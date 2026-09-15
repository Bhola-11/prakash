from django.contrib import admin, messages
from django.urls import path
from django.shortcuts import redirect
from django.utils.html import format_html
from .models import Manufacturer, HealthCategory, HealthCondition, Medicine, MedicineImage, CategoryImage
from .image_sync import sync_medicine_images

@admin.register(Manufacturer)
class ManufacturerAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ('name',)

class CategoryImageInline(admin.TabularInline):
    model = CategoryImage
    extra = 1
    readonly_fields = ('image_preview',)

    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="height: 50px; width: 50px; object-fit: contain;" />', obj.image.url)
        return "-"
    image_preview.short_description = 'Preview'

@admin.register(HealthCategory)
class HealthCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'source_folder', 'images_count')
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ('name', 'source_folder')
    inlines = [CategoryImageInline]
    actions = ['sync_images_action']

    def images_count(self, obj):
        return obj.category_images.count()
    images_count.short_description = 'Total Images'

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('sync-images/', self.admin_site.admin_view(self.sync_images_view), name='catalogue_healthcategory_sync'),
        ]
        return custom_urls + urls

    def sync_images_view(self, request):
        stats = sync_medicine_images()
        self.message_user(
            request,
            f"Image Sync Completed — Total Scanned: {stats['total_scanned']} | New Imported: {stats['new_imported']} | Duplicates Skipped: {stats['duplicates_skipped']} | Updated: {stats['updated_images']} | Invalid: {stats['invalid_files']} | Errors: {stats['errors']}",
            level=messages.SUCCESS
        )
        return redirect('..')

    @admin.action(description='Sync Category Images with Strict Deduplication')
    def sync_images_action(self, request, queryset):
        stats = sync_medicine_images()
        self.message_user(
            request,
            f"Image Sync Completed — Total Scanned: {stats['total_scanned']} | New Imported: {stats['new_imported']} | Duplicates Skipped: {stats['duplicates_skipped']} | Updated: {stats['updated_images']}",
            level=messages.SUCCESS
        )

@admin.register(CategoryImage)
class CategoryImageAdmin(admin.ModelAdmin):
    list_display = ('file_name', 'category', 'short_hash', 'file_size_kb', 'is_primary', 'is_active', 'image_preview', 'updated_at')
    list_filter = ('category', 'is_primary', 'is_active')
    search_fields = ('file_name', 'image_hash', 'category__name')
    list_editable = ('is_primary', 'is_active')
    readonly_fields = ('image_hash', 'file_size', 'image_preview')

    def short_hash(self, obj):
        return obj.image_hash[:12] + '...' if obj.image_hash else '-'
    short_hash.short_description = 'SHA-256 Hash'

    def file_size_kb(self, obj):
        return f"{obj.file_size / 1024:.1f} KB" if obj.file_size else '-'
    file_size_kb.short_description = 'Size'

    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="height: 50px; width: 50px; object-fit: contain;" />', obj.image.url)
        return "-"
    image_preview.short_description = 'Preview'

@admin.register(HealthCondition)
class HealthConditionAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'slug')
    prepopulated_fields = {'slug': ('name',)}
    list_filter = ('category',)
    search_fields = ('name',)

class MedicineImageInline(admin.TabularInline):
    model = MedicineImage
    extra = 1

@admin.register(Medicine)
class MedicineAdmin(admin.ModelAdmin):
    list_display = ('name', 'form', 'manufacturer', 'category', 'is_featured', 'is_active')
    list_filter = ('is_featured', 'is_active', 'form', 'manufacturer', 'category')
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ('name', 'generic_name', 'manufacturer__name')
    inlines = [MedicineImageInline]
    filter_horizontal = ('categories', 'conditions')
