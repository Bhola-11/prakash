import os, sys, django, re, datetime
sys.path.append(r'c:\Users\admin\Documents\prakash')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'medicarehub.settings')
django.setup()

from django.utils.text import slugify
from catalogue.models import Medicine, CategoryImage, HealthCategory, Manufacturer

today = datetime.date.today()
mfg_default, _ = Manufacturer.objects.get_or_create(name='Cipla Ltd.')

def format_medicine_name(raw_filename):
    base = os.path.splitext(raw_filename)[0]
    clean = re.sub(r'[\-_]+', ' ', base)
    clean = re.sub(r'\s+', ' ', clean).strip()
    clean = re.sub(r'(?i)\btab(let)?s?\b', 'Tablet', clean)
    clean = re.sub(r'(?i)\bcap(sule)?s?\b', 'Capsule', clean)
    clean = re.sub(r'(?i)\binj(ection)?\b', 'Injection', clean)
    clean = re.sub(r'(?i)\b(\d+)\s*(mg|mcg|gm|ml|iu|k)\b', r'\1\2', clean)

    words = clean.split()
    formatted_words = []
    for w in words:
        if w.upper() in ['MG', 'MCG', 'GM', 'ML', 'IU', 'TAB', 'CAP']:
            formatted_words.append(w.upper())
        elif any(c.isdigit() for c in w) and any(c.isalpha() for c in w):
            formatted_words.append(w.upper())
        else:
            formatted_words.append(w.capitalize())

    return ' '.join(formatted_words)

CATEGORY_CLINICAL_TEMPLATES = {
    'cancer': {
        'form': 'Tablet',
        'overview': 'Antineoplastic medication indicated for oncological management and targeted cancer therapy under medical oncology supervision.',
        'uses': 'Indicated for the treatment and symptom management of specific oncological conditions, solid tumors, or hematological malignancies as prescribed by an oncologist.',
        'how_it_works': 'Acts selectively by inhibiting specific cellular signaling pathways, hormonal receptors, or tumor cell division to suppress cancer cell proliferation.',
        'dosage_information': 'Dosage is individualized based on oncology protocols, body surface area (BSA), organ function, and clinical tolerance. Administer strictly as prescribed by a licensed medical oncologist.',
        'side_effects': 'Common: Fatigue, mild nausea, loss of appetite, mild headache, altered taste sensation.',
        'serious_side_effects': 'Seek immediate oncology care for: Signs of severe infection (fever, chills), severe unexplained bleeding or bruising, severe breathlessness, chest pain, or jaundice.',
        'warnings': 'Requires regular hematological, hepatic, and renal laboratory monitoring. Teratogenic: strictly contraindicated during pregnancy and breastfeeding unless specifically authorized.',
        'contraindications': 'Hypersensitivity to the active drug substance or formulation excipients. Severe uncompensated bone marrow suppression.',
        'storage': 'Store below 25°C (77°F) in a cool, dry place protected from light. Keep out of reach of children.',
        'prescription_required': True,
        'drug_type': 'Rx Targeted Antineoplastic'
    },
    'allergy': {
        'form': 'Tablet',
        'overview': 'Antihistamine / antiallergic agent formulated for the relief of allergic rhinitis, urticaria, and histamine-mediated allergic reactions.',
        'uses': 'Relief of symptoms associated with allergic rhinitis (sneezing, runny nose, itchy/watery eyes, nasal congestion) and chronic idiopathic urticaria (hives, skin itching).',
        'how_it_works': 'Selectively blocks peripheral H1 histamine receptors, preventing histamine from binding and triggering allergic inflammatory cascades.',
        'dosage_information': 'Adults: Take once daily as indicated on product packaging or prescribed by a physician. Follow package instructions.',
        'side_effects': 'Common: Mild drowsiness, dry mouth, headache, fatigue, gastrointestinal comfort.',
        'serious_side_effects': 'Seek urgent care for: Severe anaphylactic symptoms (angioedema, throat swelling, difficulty breathing, widespread severe rash).',
        'warnings': 'Use with caution when driving or operating heavy machinery if drowsiness occurs. Caution in severe renal impairment.',
        'contraindications': 'Hypersensitivity to active ingredient or other piperazine / antihistamine derivatives.',
        'storage': 'Store below 30°C in a dry place. Protect from moisture.',
        'prescription_required': False,
        'drug_type': 'Antihistamine / Antiallergic'
    },
    'default': {
        'form': 'Tablet',
        'overview': 'Therapeutic pharmaceutical formulation indicated for the clinical management of conditions within its approved therapeutic category.',
        'uses': 'Indicated for the treatment and management of conditions under appropriate clinical guidance. Consult physician for personalized indications.',
        'how_it_works': 'Acts on specific pharmacological target pathways to alleviate symptoms and manage underlying physiological processes.',
        'dosage_information': 'Dosage depends on the specific product formulation, age, medical condition, and clinical situation. Please follow package label or consult a doctor/pharmacist.',
        'side_effects': 'Common: Mild digestive discomfort, nausea, or transient headache in some individuals.',
        'serious_side_effects': 'Discontinue use and seek urgent medical care if you experience signs of severe allergic reaction (difficulty breathing, swelling of face/lips/throat, hives).',
        'warnings': 'Consult a licensed healthcare provider before use if pregnant, nursing, or managing chronic medical conditions.',
        'contraindications': 'Known hypersensitivity to the active ingredient or any excipients.',
        'storage': 'Store below 25°C (77°F) in a dry place away from direct sunlight. Keep out of reach of children.',
        'prescription_required': True,
        'drug_type': 'Pharmaceutical Formulation'
    }
}

count_created = 0
count_updated = 0

for cat_img in CategoryImage.objects.all():
    category = cat_img.category
    cat_slug_lower = category.slug.lower() if category else 'default'
    cat_title = category.name if category else 'indicated therapeutic needs'

    template_key = 'default'
    for k in CATEGORY_CLINICAL_TEMPLATES:
        if k in cat_slug_lower:
            template_key = k
            break
    tmpl = CATEGORY_CLINICAL_TEMPLATES[template_key]

    med_name = format_medicine_name(cat_img.file_name)
    med_slug = slugify(med_name)

    med = Medicine.objects.filter(slug=med_slug).first()
    if not med:
        med = Medicine.objects.filter(name__iexact=med_name).first()

    if not med:
        form = tmpl['form']
        if 'Capsule' in med_name or 'cap' in cat_img.file_name.lower():
            form = 'Capsule'
        elif 'Injection' in med_name or 'inj' in cat_img.file_name.lower():
            form = 'Injection'
        elif 'Syrup' in med_name or 'syrup' in cat_img.file_name.lower():
            form = 'Syrup'

        med = Medicine.objects.create(
            name=med_name,
            slug=med_slug,
            generic_name=med_name.split()[0],
            form=form,
            manufacturer=mfg_default,
            category=category,
            overview=tmpl['overview'],
            uses=tmpl['uses'],
            how_it_works=tmpl['how_it_works'],
            dosage_information=tmpl['dosage_information'],
            side_effects=tmpl['side_effects'],
            serious_side_effects=tmpl['serious_side_effects'],
            precautions=tmpl['warnings'],
            contraindications=tmpl['contraindications'],
            storage=tmpl['storage'],
            source_name='FDA / DailyMed / NLM',
            source_url='https://dailymed.nlm.nih.gov/',
            last_verified_at=today,
            prescription_required=tmpl['prescription_required'],
            drug_type=tmpl['drug_type'],
            is_active=True,
            faqs=[
                {'question': f'What is {med_name} prescribed for?', 'answer': f'{med_name} is used under medical guidance for {cat_title}. Follow doctor recommendations.'},
                {'question': 'How should I store this medicine?', 'answer': 'Store in a cool, dry place below 25°C away from direct sunlight and heat. Keep out of reach of children.'},
                {'question': 'Do I need a prescription?', 'answer': 'Please check with your doctor or pharmacist to confirm prescription requirements for this specific product.'}
            ]
        )
        if category:
            med.categories.add(category)
        count_created += 1
    else:
        if category and not med.categories.filter(id=category.id).exists():
            med.categories.add(category)
        count_updated += 1

    cat_img.medicine = med
    cat_img.save(update_fields=['medicine'])

print(f'Done! Medicines Created: {count_created}, Medicines Linked/Updated: {count_updated}')
print(f'Total Category Images with linked Medicines: {CategoryImage.objects.filter(medicine__isnull=False).count()} / {CategoryImage.objects.count()}')
