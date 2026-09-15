import os
import shutil
import hashlib
import logging
from pathlib import Path
from PIL import Image
from django.conf import settings
from django.db import transaction, IntegrityError
from django.utils.text import slugify
from .models import HealthCategory, CategoryImage

logger = logging.getLogger(__name__)

SUPPORTED_EXTENSIONS = {'.jpg', '.jpeg', '.png', '.webp', '.avif', '.gif'}

def compute_file_sha256(file_path):
    """
    Computes SHA-256 hash of a file's binary content.
    Used for 100% accurate, content-based duplicate detection.
    """
    hasher = hashlib.sha256()
    with open(file_path, 'rb') as f:
        for chunk in iter(lambda: f.read(65536), b''):
            hasher.update(chunk)
    return hasher.hexdigest()

def clean_category_name(raw_name):
    """
    Clean and normalize category folder names.
    Examples:
        'ALLERGY MEDICINE' -> 'Allergy Medicine'
        'BIRTH COUTROL MEDICINE' -> 'Birth Control Medicine'
        'Antidepressants MEDICINE' -> 'Antidepressants Medicine'
    """
    name = raw_name.strip()
    name = ' '.join(name.split())
    if 'COUTROL' in name.upper():
        name = name.replace('COUTROL', 'Control').replace('coutrol', 'Control')
    return name.title()

def validate_image_file(file_path):
    """
    Validate that the file is an actual readable image.
    Never modify or delete the source file.
    """
    try:
        ext = os.path.splitext(file_path)[1].lower()
        if ext not in SUPPORTED_EXTENSIONS:
            return False, "Unsupported extension"
        
        file_size = os.path.getsize(file_path)
        if file_size == 0:
            return False, "Empty file"

        with Image.open(file_path) as img:
            img.verify()
        return True, "Valid image"
    except Exception as e:
        return False, str(e)

def sync_medicine_images(source_dir=None):
    """
    Scans the medicine images directory with strict SHA-256 duplicate prevention.
    ONE UNIQUE IMAGE CONTENT = ONE IMAGE RECORD / PHYSICAL IMAGE.
    """
    if not source_dir:
        source_dir = getattr(
            settings,
            'MEDICINE_IMAGE_ROOT',
            r'C:\Users\admin\Documents\Resume-project\EXPORT MEDICINES\EXPORT MEDICINES'
        )

    stats = {
        'total_scanned': 0,
        'new_imported': 0,
        'duplicates_skipped': 0,
        'updated_images': 0,
        'invalid_files': 0,
        'errors': 0,
        'categories_found': 0,
        'categories_summary': []
    }

    source_path = Path(source_dir)
    if not source_path.exists() or not source_path.is_dir():
        logger.error(f"Source directory not found: {source_dir}")
        return stats

    media_root = Path(settings.MEDIA_ROOT)
    dest_base = media_root / 'category_images'
    dest_base.mkdir(parents=True, exist_ok=True)

    # Scan top-level subdirectories as categories
    for entry in sorted(os.listdir(source_path)):
        cat_dir = source_path / entry
        if not cat_dir.is_dir():
            continue

        stats['categories_found'] += 1
        raw_cat_name = entry
        cleaned_cat_name = clean_category_name(raw_cat_name)
        cat_slug = slugify(cleaned_cat_name)

        # Match or create HealthCategory
        category = HealthCategory.objects.filter(slug=cat_slug).first()
        if not category:
            category = HealthCategory.objects.filter(name__iexact=cleaned_cat_name).first()
        if not category:
            base_keyword = cleaned_cat_name.lower().replace('medicine', '').strip()
            if base_keyword:
                category = HealthCategory.objects.filter(name__icontains=base_keyword).first()

        if not category:
            category = HealthCategory.objects.create(
                name=cleaned_cat_name,
                slug=cat_slug,
                source_folder=raw_cat_name,
                description=f"Medicines and treatments for {cleaned_cat_name}."
            )
        else:
            if not category.source_folder:
                category.source_folder = raw_cat_name
                category.save(update_fields=['source_folder'])

        cat_imported = 0
        cat_duplicates = 0
        cat_skipped = 0
        cat_updated = 0

        target_cat_dir = dest_base / category.slug
        target_cat_dir.mkdir(parents=True, exist_ok=True)

        # Recursively scan all files in category folder
        for root, _, filenames in os.walk(cat_dir):
            for fname in sorted(filenames):
                stats['total_scanned'] += 1
                src_file_path = Path(root) / fname

                is_valid, reason = validate_image_file(src_file_path)
                if not is_valid:
                    stats['invalid_files'] += 1
                    cat_skipped += 1
                    continue

                try:
                    # 1. Compute Cryptographic Content Hash (SHA-256)
                    file_hash = compute_file_sha256(src_file_path)
                    file_size = src_file_path.stat().st_size

                    # 2. Strict Content-Based Duplicate Check
                    existing_by_hash = CategoryImage.objects.filter(image_hash=file_hash).first()

                    if existing_by_hash:
                        # Content already exists in DB! NEVER create duplicate physical file or DB record.
                        stats['duplicates_skipped'] += 1
                        cat_duplicates += 1

                        # Associate existing image with current category if not already linked
                        if not existing_by_hash.categories.filter(id=category.id).exists():
                            existing_by_hash.categories.add(category)
                            stats['updated_images'] += 1
                            cat_updated += 1

                        if not existing_by_hash.category:
                            existing_by_hash.category = category
                            existing_by_hash.save(update_fields=['category'])

                        if not existing_by_hash.is_active:
                            existing_by_hash.is_active = True
                            existing_by_hash.save(update_fields=['is_active'])

                        continue

                    # 3. New Unique Image: Copy to storage and register in DB
                    safe_fname = fname.replace(' ', '_')
                    dest_file_path = target_cat_dir / safe_fname
                    rel_media_path = f"category_images/{category.slug}/{safe_fname}"

                    if not dest_file_path.exists() or dest_file_path.stat().st_size != file_size:
                        shutil.copy2(src_file_path, dest_file_path)

                    is_first = not category.category_images.exists() and not category.all_category_images.exists()

                    with transaction.atomic():
                        new_img = CategoryImage.objects.create(
                            category=category,
                            image=rel_media_path,
                            image_hash=file_hash,
                            file_size=file_size,
                            file_name=fname,
                            file_path=str(src_file_path),
                            is_primary=is_first,
                            is_active=True
                        )
                        new_img.categories.add(category)

                    stats['new_imported'] += 1
                    cat_imported += 1

                except IntegrityError:
                    # Concurrent execution protection: if inserted concurrently, fetch & link
                    existing_by_hash = CategoryImage.objects.filter(image_hash=file_hash).first()
                    if existing_by_hash:
                        existing_by_hash.categories.add(category)
                        stats['duplicates_skipped'] += 1
                        cat_duplicates += 1
                except Exception as e:
                    logger.error(f"Error processing {src_file_path}: {e}")
                    stats['errors'] += 1

        stats['categories_summary'].append({
            'name': category.name,
            'source_folder': raw_cat_name,
            'imported': cat_imported,
            'duplicates': cat_duplicates,
            'updated': cat_updated,
            'skipped': cat_skipped,
            'total_images': CategoryImage.objects.filter(categories=category).count()
        })

    return stats
