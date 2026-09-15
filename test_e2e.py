import os
import django
from django.test import Client
from django.urls import reverse
import sys

# Setup django environment
sys.path.append('c:/Users/admin/Documents/prakash')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'medicarehub.settings')
django.setup()

from catalogue.models import Medicine, HealthCategory, HealthCondition

def run_checks():
    client = Client()
    
    # Get some sample data
    med = Medicine.objects.filter(is_active=True).first()
    cat = HealthCategory.objects.first()
    cond = HealthCondition.objects.filter(category=cat).first() if cat else None
    
    urls_to_test = [
        ('/', 'Home'),
        ('/medicines/', 'All Medicines'),
        ('/health-categories/', 'Health Categories'),
        ('/search/?q=paracetamol', 'Search'),
        ('/about/', 'About'),
        ('/contact/', 'Contact'),
    ]
    
    if med:
        urls_to_test.append((f'/medicines/{med.slug}/', 'Medicine Detail'))
    
    if cat:
        urls_to_test.append((f'/health-categories/{cat.slug}/', 'Category Detail'))
        
    if cond:
        urls_to_test.append((f'/health-categories/{cat.slug}/{cond.slug}/', 'Condition Detail'))

    print("--- End to End URL Check ---")
    all_passed = True
    for url, name in urls_to_test:
        response = client.get(url)
        if response.status_code == 200:
            print(f"PASS: {name} ({url}) returned 200 OK")
        else:
            print(f"FAIL: {name} ({url}) returned {response.status_code}")
            all_passed = False
            
    print("----------------------------")
    if all_passed:
        print("All endpoints are working successfully!")
    else:
        print("Some endpoints failed. Please check the errors.")

if __name__ == '__main__':
    run_checks()
