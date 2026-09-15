from django.core.management.base import BaseCommand
from catalogue.models import Manufacturer, HealthCategory, HealthCondition, Medicine, MedicineImage
from django.utils.text import slugify
import random

class Command(BaseCommand):
    help = 'Seed the database with initial sample data'

    def handle(self, *args, **kwargs):
        self.stdout.write('Seeding data...')
        
        # Clear existing data
        Manufacturer.objects.all().delete()
        HealthCategory.objects.all().delete()
        HealthCondition.objects.all().delete()
        Medicine.objects.all().delete()
        
        # Manufacturers
        manufacturers = [
            'Cipla Ltd.', 'Sun Pharmaceutical', 'Dr. Reddy\'s Laboratories', 
            'Torrent Pharmaceuticals', 'Alkem Laboratories', 'Micro Labs', 'Abbott', 'GSK Consumer'
        ]
        mfg_objs = {}
        for m in manufacturers:
            mfg_objs[m] = Manufacturer.objects.create(name=m)
            
        # Categories
        categories_data = [
            {'name': 'Cancer', 'desc': 'Medicines for different types of cancer', 'types': 10},
            {'name': 'Vitamins & Supplements', 'desc': 'Essential vitamins and nutritional supplements', 'types': 8},
            {'name': 'Diabetes', 'desc': 'Medicines for Type 1, Type 2 and related conditions', 'types': 5},
            {'name': 'Heart Health', 'desc': 'Medicines for BP, cholesterol and heart conditions', 'types': 6},
            {'name': 'Respiratory Health', 'desc': 'Medicines for cough, cold, asthma and more', 'types': 6},
            {'name': 'Sexual Health', 'desc': 'Medicines for sexual wellness and related conditions', 'types': 7},
            {'name': 'Digestive Health', 'desc': 'Medicines for acidity, gas, liver and digestion', 'types': 6},
            {'name': 'Kidney Health', 'desc': 'Medicines for kidney care and related problems', 'types': 6},
            {'name': 'Skin Health', 'desc': 'Medicines for acne, allergy, infections and more', 'types': 7},
            {'name': 'Eye Care', 'desc': 'Medicines for eye infections, dryness and more', 'types': 5},
            {'name': 'Women\'s Health', 'desc': 'Medicines for women\'s health', 'types': 9},
            {'name': 'Pain Relief', 'desc': 'Medicines for pain relief', 'types': 6},
        ]
        
        cat_objs = {}
        for c in categories_data:
            cat_objs[c['name']] = HealthCategory.objects.create(name=c['name'], description=c['desc'])
            
        # Conditions
        conditions_data = {
            'Cancer': ['Breast Cancer', 'Lung Cancer', 'Blood Cancer', 'Prostate Cancer', 'Colon Cancer'],
            'Vitamins & Supplements': ['Vitamin D Deficiency', 'Iron Deficiency', 'B12 Deficiency'],
            'Diabetes': ['Type 1 Diabetes', 'Type 2 Diabetes', 'Gestational Diabetes'],
            'Heart Health': ['High Blood Pressure', 'High Cholesterol', 'Heart Failure'],
            'Respiratory Health': ['Asthma', 'COPD', 'Bronchitis'],
            'Pain Relief': ['Headache', 'Fever', 'Muscle Pain', 'Joint Pain']
        }
        
        cond_objs = {}
        for cat_name, conds in conditions_data.items():
            cat = cat_objs[cat_name]
            for cond in conds:
                cond_objs[cond] = HealthCondition.objects.create(name=cond, category=cat)
                
        # Medicines
        medicines_data = [
            {
                'name': 'Paracetamol 500mg',
                'generic': 'Paracetamol',
                'form': 'Tablet',
                'mfg': 'Cipla Ltd.',
                'cat': 'Pain Relief',
                'cond': 'Fever',
                'desc': 'Used for pain relief and fever.',
                'pack': '10 Tablets in 1 Strip'
            },
            {
                'name': 'Azithromycin 500mg',
                'generic': 'Azithromycin',
                'form': 'Tablet',
                'mfg': 'Alkem Laboratories',
                'cat': 'Respiratory Health',
                'cond': 'Bronchitis',
                'desc': 'Antibiotic used to treat various bacterial infections.',
                'pack': '5 Tablets in 1 Strip'
            },
            {
                'name': 'Omeprazole 20mg',
                'generic': 'Omeprazole',
                'form': 'Capsule',
                'mfg': 'Sun Pharmaceutical',
                'cat': 'Digestive Health',
                'cond': None,
                'desc': 'Used to treat GERD and stomach ulcers.',
                'pack': '15 Capsules in 1 Strip'
            },
            {
                'name': 'Vitamin D3 60K',
                'generic': 'Cholecalciferol 60,000 IU',
                'form': 'Tablet',
                'mfg': 'Abbott',
                'cat': 'Vitamins & Supplements',
                'cond': 'Vitamin D Deficiency',
                'desc': 'Vitamin D supplement.',
                'pack': '4 Tablets in 1 Strip'
            },
            {
                'name': 'Letrozole 2.5mg',
                'generic': 'Letrozole IP 2.5mg',
                'form': 'Tablet',
                'mfg': 'Cipla Ltd.',
                'cat': 'Cancer',
                'cond': 'Breast Cancer',
                'desc': 'Letrozole is used in the treatment of hormone receptor positive breast cancer in postmenopausal women.',
                'overview': 'Letrozole is used in the treatment of hormone receptor positive breast cancer in postmenopausal women. It belongs to a group of medicines called aromatase inhibitors.',
                'uses': 'Treatment of hormone receptor positive breast cancer\nUsed as adjuvant therapy',
                'how_it_works': 'Letrozole works by reducing the amount of estrogen in the body.',
                'pack': '10 Tablets in 1 Strip',
                'rx': True,
                'drug_type': 'Aromatase Inhibitor',
                'preg': 'D'
            }
        ]
        
        # Add 100 more random medicines for pagination
        forms = ['Tablet', 'Capsule', 'Syrup', 'Injection', 'Drops']
        for i in range(1, 120):
            medicines_data.append({
                'name': f'GenericMed {i}00mg',
                'generic': f'Active Ingredient {i}',
                'form': random.choice(forms),
                'mfg': random.choice(manufacturers),
                'cat': random.choice(list(cat_objs.keys())),
                'cond': None,
                'desc': 'Generic placeholder description.',
                'pack': '10 per strip'
            })
            
        for m in medicines_data:
            cat = cat_objs.get(m['cat']) if m.get('cat') else None
            cond = cond_objs.get(m['cond']) if m.get('cond') else None
            
            med = Medicine.objects.create(
                name=m['name'],
                generic_name=m.get('generic', ''),
                form=m.get('form', ''),
                manufacturer=mfg_objs[m['mfg']],
                category=cat,
                subcategory=cond,
                description=m.get('desc', ''),
                overview=m.get('overview', ''),
                uses=m.get('uses', ''),
                how_it_works=m.get('how_it_works', ''),
                pack_size=m.get('pack', ''),
                prescription_required=m.get('rx', False),
                drug_type=m.get('drug_type', ''),
                pregnancy_category=m.get('preg', ''),
                is_featured=True if 'Paracetamol' in m['name'] or 'Letrozole' in m['name'] or 'Vitamin' in m['name'] else False
            )
            if cat:
                med.categories.add(cat)
            if cond:
                med.conditions.add(cond)
                
        self.stdout.write(self.style.SUCCESS('Successfully seeded database.'))
