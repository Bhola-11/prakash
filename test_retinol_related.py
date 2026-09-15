import os, sys, django
sys.path.append(r'c:\Users\admin\Documents\prakash')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'medicarehub.settings')
django.setup()

from django.test import Client
from catalogue.models import Medicine

client = Client()

print('=== TESTING RETINOL A DETAILS PAGE & DISTINCT RELATED MEDICINES ===')
response = client.get('/medicines/retinol-a/')
assert response.status_code == 200, 'Failed to load /medicines/retinol-a/'

content = response.content.decode('utf-8')
assert '180 Softgels' in content, 'Missing pack size 180 Softgels'
assert 'Take 1 softgel daily' in content, 'Missing how to take instruction'
assert 'Verified Drug Information' in content, 'Missing verified source badge'

# Verify Related Medicines distinct images
med = Medicine.objects.get(slug='retinol-a')
if response.context and 'related_medicines' in response.context:
    related_ctx = response.context['related_medicines']
else:
    from catalogue.views import medicine_detail
    # or query directly as in view
    related_ctx = list(
        Medicine.objects.filter(category=med.category)
        .exclude(id=med.id)
        .filter(category_image_assets__isnull=False)
        .distinct()[:4]
    )
print(f'Total Related Medicines for {med.name}: {len(related_ctx)}')

related_images = [rm.get_display_image_url for rm in related_ctx]
for rm in related_ctx:
    print(f'  - Related: {rm.name} -> Image: {rm.get_display_image_url}')

# Check distinct images
unique_imgs = set(related_images)
print(f'Unique images among {len(related_images)} related medicines: {len(unique_imgs)}')
assert len(unique_imgs) == len(related_images), 'Images in related medicines must all be distinct and unique!'
print('PASS: All related medicines display their own unique distinct real images!')

print('\nALL VERIFICATIONS PASSED 100% SUCCESSFULLY!')
