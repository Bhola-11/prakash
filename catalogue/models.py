from django.db import models
from django.utils.text import slugify

class Manufacturer(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

class HealthCategory(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    source_folder = models.CharField(max_length=255, blank=True)
    description = models.TextField(blank=True)
    icon = models.ImageField(upload_to='categories/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Health Categories"

class CategoryImage(models.Model):
    category = models.ForeignKey(HealthCategory, on_delete=models.CASCADE, related_name='category_images', null=True, blank=True)
    categories = models.ManyToManyField(HealthCategory, related_name='all_category_images', blank=True)
    medicine = models.ForeignKey('Medicine', on_delete=models.SET_NULL, null=True, blank=True, related_name='category_image_assets')
    image = models.ImageField(upload_to='category_images/')
    image_hash = models.CharField(max_length=64, unique=True, db_index=True)
    file_name = models.CharField(max_length=255)
    file_path = models.CharField(max_length=500, blank=True)
    file_size = models.BigIntegerField(default=0)
    is_primary = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-is_primary', 'file_name']

    @property
    def clean_title(self):
        import os, re
        base = os.path.splitext(self.file_name)[0]
        # Clean up common file patterns (e.g. TAB, CAP, underscores)
        base = re.sub(r'[\-_]+', ' ', base)
        base = re.sub(r'\s+', ' ', base).strip()
        return base.title()

    @property
    def get_medicine_slug(self):
        if self.medicine:
            return self.medicine.slug
        from django.utils.text import slugify
        return slugify(self.clean_title)

    def __str__(self):
        cat_name = self.category.name if self.category else "Uncategorized"
        return f"{cat_name} - {self.file_name} ({self.image_hash[:8]})"

class HealthCondition(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    description = models.TextField(blank=True)
    category = models.ForeignKey(HealthCategory, on_delete=models.CASCADE, related_name='conditions')
    icon = models.ImageField(upload_to='conditions/', blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

class Medicine(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    generic_name = models.CharField(max_length=255, blank=True)
    composition = models.TextField(blank=True)
    form = models.CharField(max_length=100, blank=True) # e.g. Tablet, Capsule, Syrup
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE, related_name='medicines')
    
    # Categories and Conditions
    category = models.ForeignKey(HealthCategory, on_delete=models.SET_NULL, null=True, blank=True, related_name='primary_medicines')
    subcategory = models.ForeignKey(HealthCondition, on_delete=models.SET_NULL, null=True, blank=True, related_name='primary_medicines')
    
    categories = models.ManyToManyField(HealthCategory, related_name='all_medicines', blank=True)
    conditions = models.ManyToManyField(HealthCondition, related_name='all_medicines', blank=True)
    
    description = models.TextField(blank=True)
    overview = models.TextField(blank=True)
    uses = models.TextField(blank=True)
    how_it_works = models.TextField(blank=True)
    side_effects = models.TextField(blank=True)
    precautions = models.TextField(blank=True)
    storage = models.TextField(blank=True)
    also_known_as = models.CharField(max_length=255, blank=True)
    pack_size = models.CharField(max_length=100, blank=True)
    
    brand_name = models.CharField(max_length=255, blank=True)
    strength = models.CharField(max_length=100, blank=True)
    route = models.CharField(max_length=100, default='Oral', blank=True)
    active_ingredients = models.TextField(blank=True)
    inactive_ingredients = models.TextField(blank=True)
    dosage_information = models.TextField(blank=True)
    serious_side_effects = models.TextField(blank=True)
    contraindications = models.TextField(blank=True)
    interactions = models.TextField(blank=True)
    
    # Verification & Source metadata
    source_name = models.CharField(max_length=255, default='FDA / DailyMed / NLM', blank=True)
    source_url = models.URLField(max_length=500, default='https://dailymed.nlm.nih.gov/', blank=True)
    last_verified_at = models.DateField(null=True, blank=True)
    faqs = models.JSONField(default=list, blank=True)
    
    prescription_required = models.BooleanField(default=False)
    drug_type = models.CharField(max_length=100, blank=True)
    habit_forming = models.BooleanField(default=False)
    pregnancy_category = models.CharField(max_length=50, blank=True)
    alcohol_interaction = models.CharField(max_length=255, blank=True)
    
    is_featured = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        if not self.strength and any(c.isdigit() for c in self.name):
            import re
            m = re.search(r'\b\d+(\.\d+)?\s*(mg|mcg|gm|ml|iu|k)?\b', self.name, re.IGNORECASE)
            if m:
                self.strength = m.group(0).strip()
        super().save(*args, **kwargs)

    @property
    def get_display_image_url(self):
        # Tier 1: Directly linked real CategoryImage asset
        direct_asset = self.category_image_assets.filter(is_active=True).first()
        if direct_asset and direct_asset.image:
            return direct_asset.image.url

        # Explicit MedicineImage if present
        first_img = self.images.filter(is_primary=True).first() or self.images.first()
        if first_img and first_img.image:
            return first_img.image.url

        # Determine category
        cat_to_check = self.category
        if not cat_to_check and self.categories.exists():
            cat_to_check = self.categories.first()

        # Tier 2: Exact or high-confidence keyword match in real CategoryImages
        import re
        med_keywords = [
            w.lower() for w in re.split(r'[\s\-_,]+', self.name + ' ' + (self.generic_name or ''))
            if len(w) > 2 and not re.match(r'^\d+(mg|ml|gm|mcg|k)?$', w.lower())
        ]

        from .models import CategoryImage
        if cat_to_check and med_keywords:
            cat_images = CategoryImage.objects.filter(
                models.Q(category=cat_to_check) | models.Q(categories=cat_to_check),
                is_active=True
            ).distinct()

            for cat_img in cat_images:
                fn_lower = cat_img.file_name.lower()
                if any(kw in fn_lower for kw in med_keywords):
                    if cat_img.image:
                        return cat_img.image.url

        # Fallback to empty string if no authentic matching image found (never show wrong drug image)
        return ""

    def __str__(self):
        return self.name

class MedicineImage(models.Model):
    medicine = models.ForeignKey(Medicine, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='medicines/')
    is_primary = models.BooleanField(default=False)

    def __str__(self):
        return f"Image for {self.medicine.name}"
