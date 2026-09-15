from django.core.management.base import BaseCommand
from catalogue.image_sync import sync_medicine_images

class Command(BaseCommand):
    help = 'Scan main medicine images folder and sync category images with strict SHA-256 duplicate prevention'

    def add_arguments(self, parser):
        parser.add_argument(
            '--source-dir',
            type=str,
            default=None,
            help='Path to the source folder containing medicine category images'
        )

    def handle(self, *args, **options):
        source_dir = options.get('source_dir')
        self.stdout.write(self.style.NOTICE('Starting strict content-hash medicine images synchronization...'))

        stats = sync_medicine_images(source_dir=source_dir)

        self.stdout.write(self.style.SUCCESS('\n========================================'))
        self.stdout.write(self.style.SUCCESS('Image Sync Completed'))
        self.stdout.write(self.style.SUCCESS('========================================'))
        self.stdout.write(f"Total Scanned:      {stats['total_scanned']}")
        self.stdout.write(f"New Imported:       {stats['new_imported']}")
        self.stdout.write(f"Duplicates Skipped: {stats['duplicates_skipped']}")
        self.stdout.write(f"Updated:            {stats['updated_images']}")
        self.stdout.write(f"Invalid / Skipped:  {stats['invalid_files']}")
        self.stdout.write(f"Errors:             {stats['errors']}")
        self.stdout.write(self.style.SUCCESS('========================================\n'))
