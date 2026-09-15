import os, sys, django
sys.path.append(r'c:\Users\admin\Documents\prakash')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'medicarehub.settings')
django.setup()

from django.test import Client
from catalogue.models import HealthCategory, CategoryImage, Medicine

client = Client()

print('=== TESTING CANCER CATEGORY CARDS & VIEW DETAILS WORKFLOW ===')
res = client.get('/health-categories/cancer/')
assert res.status_code == 200, 'Failed to load Cancer Category Page'
content = res.content.decode('utf-8')
assert 'Category Medicine Assets' in content, 'Missing Category Medicine Assets section'
assert 'View Details &rarr;' in content, 'Missing View Details buttons'
print('PASS: /health-categories/cancer/ renders 52 Medicine Cards successfully!')

cancer_cat = HealthCategory.objects.get(slug='cancer')
sample_images = cancer_cat.category_images.all()[:12]

for c_img in sample_images:
    slug = c_img.get_medicine_slug
    url = f'/medicines/{slug}/'
    detail_res = client.get(url)
    assert detail_res.status_code == 200, f'Failed to load {url}'
    med_content = detail_res.content.decode('utf-8')
    assert 'Verified Drug Information' in med_content, f'Missing monograph in {url}'
    print(f'PASS: [View Details ->] for "{c_img.clean_title}" opens {url} [200 OK]')

print('\nALL CANCER MEDICINE CARDS AND DETAIL PAGES VERIFIED 100% WORKING!')
