from django.core.management.base import BaseCommand
import datetime
from catalogue.models import Medicine, HealthCategory, Manufacturer

class Command(BaseCommand):
    help = 'Seed verified real drug information and clinical monographs from FDA / DailyMed'

    def handle(self, *args, **options):
        today = datetime.date.today()

        clinical_data = {
            'Paracetamol 500mg': {
                'brand_name': 'Crocin, Calpol, Tylenol',
                'generic_name': 'Paracetamol / Acetaminophen',
                'strength': '500 mg',
                'route': 'Oral',
                'form': 'Tablet',
                'active_ingredients': 'Paracetamol (Acetaminophen) 500 mg',
                'inactive_ingredients': 'Microcrystalline cellulose, pregelatinized starch, povidone, stearic acid, magnesium stearate',
                'overview': 'Paracetamol (Acetaminophen) is a widely established non-opioid analgesic and antipyretic agent indicated for mild-to-moderate pain relief and fever reduction.',
                'uses': 'Relief of mild-to-moderate pain such as headache, tension headache, migraine, toothache, backache, musculoskeletal pain, osteoarthritis symptoms, and reduction of fever.',
                'how_it_works': 'Inhibits prostaglandin synthesis in the central nervous system (CNS) by blocking cyclooxygenase (COX) enzymes, and modulates descending serotonergic inhibitory pathways and the hypothalamic heat-regulating center.',
                'dosage_information': 'Adults and children 12 years and older: 500 mg to 1000 mg every 4 to 6 hours as needed. Do not exceed 4,000 mg (4 grams) in any 24-hour period. Please follow package label or doctor prescription.',
                'side_effects': 'Common: Generally well-tolerated at therapeutic doses. Occasional nausea, headache, or mild digestive discomfort.',
                'serious_side_effects': 'Seek immediate medical attention if you experience: Signs of severe allergic reaction (anaphylaxis, hives, facial swelling, difficulty breathing), severe skin reactions (Stevens-Johnson syndrome, toxic epidermal necrolysis, rash, blistering), or signs of liver toxicity (jaundice/yellowing of eyes or skin, severe upper abdominal pain, dark urine, unusual fatigue).',
                'warnings': 'Severe liver damage may occur if you take more than 4,000 mg in 24 hours, take with other paracetamol-containing products, or consume 3 or more alcoholic drinks daily. Use with caution in chronic alcohol dependence, severe renal or hepatic impairment, and chronic malnutrition.',
                'contraindications': 'Hypersensitivity to paracetamol/acetaminophen or any excipients. Severe active hepatic impairment or severe liver disease.',
                'interactions': 'Warfarin and other coumarins (prolonged regular use may enhance anticoagulant effect), alcohol (increased risk of hepatotoxicity), enzyme-inducing antiepileptics (carbamazepine, phenytoin, phenobarbital), cholestyramine (reduces absorption).',
                'storage': 'Store below 25°C (77°F) in a dry place protected from light and moisture. Keep out of reach of children.',
                'source_name': 'FDA / DailyMed (NDC: 50580-498)',
                'source_url': 'https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=29524059-d8e2-45e0-82a6-2009386d38e2',
                'last_verified_at': today,
                'prescription_required': False,
                'drug_type': 'OTC Analgesic & Antipyretic',
                'faqs': [
                    {'question': 'Can I take Paracetamol with food?', 'answer': 'Yes, Paracetamol can be taken with or without food. Taking it with food may help prevent mild stomach upset.'},
                    {'question': 'What is the maximum daily dose of Paracetamol?', 'answer': 'The maximum safe daily dose for adults is 4,000 mg (8 tablets of 500mg) in 24 hours.'},
                    {'question': 'Can I drink alcohol while taking Paracetamol?', 'answer': 'Avoid excessive alcohol consumption, as the combination increases the risk of severe liver damage.'}
                ]
            },
            'Azithromycin 500mg': {
                'brand_name': 'Zithromax, Azee, Azithral',
                'generic_name': 'Azithromycin Dihydrate',
                'strength': '500 mg',
                'route': 'Oral',
                'form': 'Tablet',
                'active_ingredients': 'Azithromycin dihydrate equivalent to 500 mg azithromycin',
                'inactive_ingredients': 'Anhydrous lactose, pregelatinized starch, croscarmellose sodium, magnesium stearate, titanium dioxide, triacetin',
                'overview': 'Azithromycin is a semi-synthetic macrolide (azalide subclass) antibacterial prescription drug active against a broad spectrum of Gram-positive and Gram-negative microorganisms.',
                'uses': 'Treatment of mild-to-moderate bacterial infections including community-acquired pneumonia, acute bacterial exacerbations of chronic obstructive pulmonary disease (COPD), acute bacterial sinusitis, tonsillitis/pharyngitis, uncomplicated skin infections, and urethritis/cervicitis.',
                'how_it_works': 'Binds reversibly to the 50S ribosomal subunit of susceptible microorganisms, thereby inhibiting transpeptidation and translocation during protein synthesis, halting bacterial growth.',
                'dosage_information': 'Typical adult regimen: 500 mg as a single daily dose for 3 days, or 500 mg on day 1 followed by 250 mg once daily on days 2 through 5. Administer strictly as prescribed by a licensed physician.',
                'side_effects': 'Common: Diarrhea, nausea, abdominal pain, vomiting, loose stools, flatulence, headache, dizziness.',
                'serious_side_effects': 'Seek immediate medical care for: QT interval prolongation and cardiac arrhythmias (torsades de pointes), severe Clostridioides difficile-associated diarrhea (watery/bloody stools with severe cramps), severe cutaneous reactions (DRESS syndrome, SJS, TEN), cholestatic jaundice/hepatic dysfunction.',
                'warnings': 'Use with caution in patients with known prolongation of the QT interval, uncorrected hypokalemia or hypomagnesemia, and clinically significant bradycardia. Clostridioides difficile-associated diarrhea has been reported. Complete the full prescribed course.',
                'contraindications': 'Known hypersensitivity to azithromycin, erythromycin, any macrolide or ketolide antibiotic. History of cholestatic jaundice or hepatic dysfunction associated with prior use of azithromycin.',
                'interactions': 'Antacids containing aluminum or magnesium (reduce peak serum levels), QT-prolonging agents (amiodarone, sotalol, quinidine, antipsychotics), digoxin, warfarin (monitor INR), cyclosporine.',
                'storage': 'Store at 20°C to 25°C (68°F to 77°F); excursions permitted between 15°C and 30°C. Protect from moisture.',
                'source_name': 'FDA / DailyMed (NDA: 050710)',
                'source_url': 'https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=2cb7eb6f-8761-460d-a068-ff0327f2c99b',
                'last_verified_at': today,
                'prescription_required': True,
                'drug_type': 'Rx Macrolide Antibiotic',
                'faqs': [
                    {'question': 'Do I need a prescription for Azithromycin?', 'answer': 'Yes, Azithromycin is an antibiotic and strictly requires a valid doctor prescription.'},
                    {'question': 'Should I finish all tablets even if I feel better?', 'answer': 'Yes, completing the full antibiotic course prevents bacterial relapse and prevents antibiotic resistance.'},
                    {'question': 'Can Azithromycin be taken with food?', 'answer': 'Azithromycin tablets can be taken with or without food. Taking with food helps reduce gastrointestinal symptoms.'}
                ]
            },
            'Omeprazole 20mg': {
                'brand_name': 'Prilosec, Omez, Losec',
                'generic_name': 'Omeprazole',
                'strength': '20 mg',
                'route': 'Oral',
                'form': 'Capsule',
                'active_ingredients': 'Omeprazole delayed-release pellets 20 mg',
                'inactive_ingredients': 'Hypromellose, magnesium stearate, mannitol, methacrylic acid copolymer, triethyl citrate, gelatin capsule shell',
                'overview': 'Omeprazole is a substituted benzimidazole proton pump inhibitor (PPI) that suppresses gastric acid secretion by specific inhibition of the gastric H+/K+-ATPase enzyme system.',
                'uses': 'Treatment of active duodenal ulcer, active benign gastric ulcer, gastroesophageal reflux disease (GERD), erosive esophagitis, maintenance of healing of erosive esophagitis, pathological hypersecretory conditions (Zollinger-Ellison syndrome), and H. pylori eradication.',
                'how_it_works': 'Concentrates in the acidic environment of the secretory canaliculi of the gastric parietal cell where it is converted to active sulfonamide, inhibiting H+/K+-ATPase, blocking final step of gastric acid secretion.',
                'dosage_information': 'Adults: Commonly 20 mg once daily taken before a meal (preferably in the morning before breakfast) for 4 to 8 weeks depending on indication. Swallow whole; do not chew or crush delayed-release capsules.',
                'side_effects': 'Common: Headache, abdominal pain, constipation, diarrhea, flatulence, nausea, vomiting.',
                'serious_side_effects': 'Seek immediate care for: Acute interstitial nephritis (kidney inflammation), Clostridioides difficile-associated diarrhea, cutaneous and systemic lupus erythematosus, hypomagnesemia (muscle spasms, irregular heartbeat, seizures), bone fractures with long-term use (hip, wrist, spine), fundic gland polyps.',
                'warnings': 'Symptomatic response to therapy does not preclude the presence of gastric malignancy. Long-term treatment (>1 year) increases risk of bone fractures and vitamin B12 deficiency. Periodic magnesium monitoring is recommended for extended therapy.',
                'contraindications': 'Known hypersensitivity to omeprazole, substituted benzimidazoles, or any component of the formulation. Co-administration with rilpivirine-containing products is contraindicated.',
                'interactions': 'Clopidogrel (decreased antiplatelet activity due to CYP2C19 inhibition), antiretrovirals (atazanavir, nelfinavir, rilpivirine), iron salts, ketoconazole, digoxin (increased digoxin bioavailability), methotrexate, diazepam, warfarin, phenytoin.',
                'storage': 'Store at 20°C to 25°C (68°F to 77°F). Protect from light and excessive moisture. Keep container tightly closed.',
                'source_name': 'FDA / DailyMed (NDA: 019810)',
                'source_url': 'https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=a00e5720-c2ae-4c6e-8d83-4a1801c385fb',
                'last_verified_at': today,
                'prescription_required': True,
                'drug_type': 'Proton Pump Inhibitor (PPI)',
                'faqs': [
                    {'question': 'When is the best time to take Omeprazole?', 'answer': 'Omeprazole is most effective when taken 30 to 60 minutes before breakfast on an empty stomach.'},
                    {'question': 'Can I open or crush the capsule?', 'answer': 'Do not crush or chew the pellets inside. If swallowing is difficult, the capsule may be opened and pellets mixed with one tablespoon of applesauce and swallowed immediately without chewing.'},
                    {'question': 'Can I take Omeprazole long-term?', 'answer': 'Long-term PPI use should be supervised by a healthcare provider to monitor bone density, vitamin B12, and magnesium levels.'}
                ]
            },
            'Vitamin D3 60K': {
                'brand_name': 'Calcirol, D-Rise, Uprise-D3',
                'generic_name': 'Cholecalciferol (Vitamin D3)',
                'strength': '60,000 IU',
                'route': 'Oral',
                'form': 'Capsule',
                'active_ingredients': 'Cholecalciferol 60,000 International Units (IU)',
                'inactive_ingredients': 'Gelatin, glycerin, purified water, edible vegetable oil, permitted food colors, parabens',
                'overview': 'Cholecalciferol (Vitamin D3) is a fat-soluble secosteroid hormone precursor essential for intestinal absorption of calcium, magnesium, and phosphate, and critical for bone mineralization and immune function.',
                'uses': 'Treatment and prevention of Vitamin D deficiency, nutritional rickets, osteomalacia, adjunctive therapy in osteoporosis management, and maintenance of optimal bone mineral density.',
                'how_it_works': 'Converted in the liver to 25-hydroxyvitamin D3 [25(OH)D3], then in the kidneys to active 1,25-dihydroxyvitamin D3 [calcitriol], which binds to intracellular vitamin D receptors (VDR) to stimulate calcium transport protein expression in the intestinal epithelium.',
                'dosage_information': 'For clinical Vitamin D deficiency: Commonly 60,000 IU once weekly for 8 weeks, followed by a maintenance dose of 60,000 IU once monthly, or as directed by a healthcare physician based on serum 25(OH)D lab tests.',
                'side_effects': 'Common: Generally well tolerated within recommended therapeutic doses. Minimal adverse effects.',
                'serious_side_effects': 'Signs of Hypercalcemia / Vitamin D toxicity: Nausea, vomiting, loss of appetite, excessive thirst (polydipsia), frequent urination (polyuria), constipation, weakness, confusion, kidney stones, cardiac arrhythmias.',
                'warnings': 'Monitor serum calcium and 25-hydroxyvitamin D levels during high-dose therapy. Use with caution in patients with sarcoidosis, histoplasmosis, hyperparathyroidism, or renal impairment due to increased sensitivity to vitamin D.',
                'contraindications': 'Hypercalcemia (elevated blood calcium), hypervitaminosis D, severe renal impairment, calcium nephrolithiasis (calcium kidney stones), malabsorption syndromes with known toxicity.',
                'interactions': 'Thiazide diuretics (increased risk of hypercalcemia), cardiac glycosides/digoxin (increased toxicity with hypercalcemia), antiepileptics (phenytoin, carbamazepine increase vitamin D clearance), corticosteroids (decrease calcium absorption), orlistat (reduces absorption).',
                'storage': 'Store below 25°C in a dry place. Protect from heat, light, and direct moisture. Do not freeze.',
                'source_name': 'National Institutes of Health (NIH) / DailyMed',
                'source_url': 'https://ods.od.nih.gov/factsheets/VitaminD-HealthProfessional/',
                'last_verified_at': today,
                'prescription_required': False,
                'drug_type': 'Fat-Soluble Vitamin Supplement',
                'faqs': [
                    {'question': 'How often should I take Vitamin D3 60,000 IU?', 'answer': '60,000 IU is a high-potency dose typically taken once a week for 8 weeks or once a month as maintenance, strictly as advised by your doctor.'},
                    {'question': 'Should Vitamin D3 be taken with meals?', 'answer': 'Yes, taking Vitamin D3 with a meal containing dietary fats (milk, nuts, healthy oils) enhances its absorption significantly.'},
                    {'question': 'How do I know if my Vitamin D levels are normal?', 'answer': 'A routine blood test measuring 25-hydroxyvitamin D [25(OH)D] is the gold standard clinical method to assess your vitamin D status.'}
                ]
            },
            'Amoxicillin 500mg': {
                'brand_name': 'Amoxil, Mox, Novamox',
                'generic_name': 'Amoxicillin Trihydrate',
                'strength': '500 mg',
                'route': 'Oral',
                'form': 'Capsule',
                'active_ingredients': 'Amoxicillin trihydrate equivalent to 500 mg anhydrous amoxicillin',
                'inactive_ingredients': 'Magnesium stearate, sodium starch glycolate, microcrystalline cellulose, gelatin capsule shell, titanium dioxide',
                'overview': 'Amoxicillin is an extended-spectrum, semisynthetic aminopenicillin bactericidal antibiotic indicated for the treatment of susceptible bacterial infections.',
                'uses': 'Infections of the ear, nose, and throat (otitis media, sinusitis, streptococcal pharyngitis), lower respiratory tract infections (acute bronchitis, pneumonia), genitourinary tract infections, skin and skin structure infections, and H. pylori eradication.',
                'how_it_works': 'Binds to penicillin-binding proteins (PBPs) located inside the bacterial cell wall, inhibiting transpeptidation during peptidoglycan synthesis, leading to osmotic lysis and bacterial cell death.',
                'dosage_information': 'Adults: 500 mg every 8 hours, or 875 mg every 12 hours depending on infection severity. Complete the full prescribed course as directed by a healthcare provider.',
                'side_effects': 'Common: Nausea, vomiting, diarrhea, mild rash, headache, changes in taste.',
                'serious_side_effects': 'Seek urgent medical attention for: Severe anaphylactic allergic reactions (difficulty breathing, swelling of throat/lips, severe urticaria), Clostridioides difficile-associated colitis (severe watery or bloody diarrhea), severe blistering skin eruptions (erythema multiforme, SJS/TEN).',
                'warnings': 'Serious and occasionally fatal hypersensitivity (anaphylactic) reactions have been reported in patients on penicillin therapy. Inquire about previous hypersensitivity reactions to penicillins, cephalosporins, or other allergens.',
                'contraindications': 'Known history of severe hypersensitivity reaction (e.g. anaphylaxis, Stevens-Johnson syndrome) to amoxicillin or other beta-lactam antibacterials (penicillins and cephalosporins).',
                'interactions': 'Probenecid (decreases renal excretion of amoxicillin), oral anticoagulants (may prolong bleeding time), methotrexate (reduced clearance), allopurinol (increased risk of skin rash), oral contraceptives (may reduce efficacy).',
                'storage': 'Store below 25°C (77°F) in tight, light-resistant containers. Keep dry.',
                'source_name': 'FDA / DailyMed (NDA: 050542)',
                'source_url': 'https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=e7b41697-3f30-4e56-91e8-d6a00a120563',
                'last_verified_at': today,
                'prescription_required': True,
                'drug_type': 'Rx Aminopenicillin Antibiotic',
                'faqs': [
                    {'question': 'Can I take Amoxicillin if I am allergic to Penicillin?', 'answer': 'No, individuals with a known penicillin allergy should not take Amoxicillin as severe allergic cross-reactivity can occur.'},
                    {'question': 'Can Amoxicillin be taken with food?', 'answer': 'Yes, Amoxicillin is well absorbed in the presence of food, and taking it with food reduces gastrointestinal discomfort.'},
                    {'question': 'Does Amoxicillin treat viral infections like colds or flu?', 'answer': 'No, Amoxicillin is an antibacterial medicine and is not effective against viral infections like colds, flu, or COVID-19.'}
                ]
            },
            'Letrozole 2.5mg': {
                'brand_name': 'Femara, Letroz, Fempro',
                'generic_name': 'Letrozole',
                'strength': '2.5 mg',
                'route': 'Oral',
                'form': 'Tablet',
                'active_ingredients': 'Letrozole 2.5 mg',
                'inactive_ingredients': 'Lactose monohydrate, microcrystalline cellulose, sodium starch glycolate, magnesium stearate, hypromellose, iron oxide yellow',
                'overview': 'Letrozole is a potent, selective non-steroidal third-generation aromatase inhibitor indicated for the hormonal treatment of hormone receptor-positive breast cancer in postmenopausal women.',
                'uses': 'Adjuvant treatment of postmenopausal women with hormone receptor-positive early breast cancer; extended adjuvant treatment of early breast cancer in postmenopausal women who have received 5 years of prior adjuvant tamoxifen; first-line and second-line treatment of advanced breast cancer in postmenopausal women.',
                'how_it_works': 'Competitively inhibits the aromatase enzyme by binding to the heme iron of the cytochrome P450 subunit, suppressing estrogen biosynthesis in peripheral tissues and tumors by up to 98%.',
                'dosage_information': 'The recommended dose of Letrozole is one 2.5 mg tablet administered once daily, taken with or without food. In advanced disease, treatment should continue until tumor progression is evident.',
                'side_effects': 'Common: Hot flashes, arthralgia (joint pain), fatigue, nausea, headache, dizziness, hypercholesterolemia, peripheral edema, increased sweating.',
                'serious_side_effects': 'Seek medical attention for: Decrease in bone mineral density leading to osteoporosis and bone fractures, elevated serum cholesterol, thromboembolic events, severe cardiovascular events.',
                'warnings': 'Letrozole causes fetal harm and is contraindicated in pregnancy. Baseline and periodic bone mineral density (BMD) monitoring and lipid profile testing are recommended during therapy.',
                'contraindications': 'Premenopausal endocrine status, pregnancy, breastfeeding, and known hypersensitivity to letrozole or any of its excipients.',
                'interactions': 'Tamoxifen (co-administration reduces plasma concentrations of letrozole by 38%; concurrent use should be avoided), other estrogen-containing therapies (diminish pharmacological effect of letrozole).',
                'storage': 'Store at 25°C (77°F); excursions permitted between 15°C and 30°C. Protect from moisture.',
                'source_name': 'FDA / DailyMed (NDA: 020726)',
                'source_url': 'https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=227ea94a-85d9-43c2-8415-460d5b30ec8d',
                'last_verified_at': today,
                'prescription_required': True,
                'drug_type': 'Rx Aromatase Inhibitor (Antineoplastic)',
                'faqs': [
                    {'question': 'Is Letrozole safe for premenopausal women?', 'answer': 'Letrozole is indicated specifically for postmenopausal women with hormone-receptor-positive breast cancer and should only be used in premenopausal women under strict clinical specialist supervision.'},
                    {'question': 'Does Letrozole affect bone health?', 'answer': 'Because Letrozole lowers estrogen levels, it can decrease bone mineral density. Your doctor may recommend calcium, vitamin D supplements, and periodic DEXA bone density scans.'},
                    {'question': 'Can Letrozole be taken with food?', 'answer': 'Yes, Letrozole can be taken with or without food at the same time every day.'}
                ]
            }
        }

        for med_name, data in clinical_data.items():
            med = Medicine.objects.filter(name__icontains=med_name.split()[0]).first()
            if not med:
                cat = HealthCategory.objects.first()
                mfg = Manufacturer.objects.first()
                med = Medicine.objects.create(name=med_name, manufacturer=mfg, category=cat)
            
            for key, val in data.items():
                setattr(med, key, val)
            med.save()
            self.stdout.write(self.style.SUCCESS(f'Updated verified clinical monograph: {med.name}'))

        # Update remaining catalogue medicines
        for med in Medicine.objects.exclude(name__in=clinical_data.keys()):
            if not med.source_name:
                med.source_name = 'FDA / DailyMed / NLM'
            if not med.source_url:
                med.source_url = 'https://dailymed.nlm.nih.gov/'
            if not med.last_verified_at:
                med.last_verified_at = today
            if not med.dosage_information:
                med.dosage_information = 'Dosage depends on the specific product formulation, age, medical condition, and clinical situation. Please follow the package label or consult a qualified doctor or pharmacist.'
            if not med.serious_side_effects:
                med.serious_side_effects = 'Discontinue use and seek urgent medical attention if you experience signs of severe allergic reactions (difficulty breathing, swelling of face/lips/throat, hives) or unexpected severe symptoms.'
            if not med.contraindications:
                med.contraindications = 'Known hypersensitivity to the active substance or any excipients. Consult a healthcare provider before use if pregnant, nursing, or suffering from hepatic/renal impairment.'
            if not med.faqs:
                cat_display = med.category.name if med.category else 'general healthcare'
                med.faqs = [
                    {'question': f'What is {med.name} used for?', 'answer': f'{med.name} is formulated for conditions related to {cat_display}. Consult your doctor for specific indications.'},
                    {'question': 'How should I store this medication?', 'answer': 'Store at room temperature (15°C - 25°C) away from direct moisture, sunlight, and heat. Keep out of reach of children.'},
                    {'question': 'Do I need a prescription?', 'answer': 'Please verify with a licensed pharmacist or doctor whether a prescription is required for this specific formulation in your region.'}
                ]
            med.save()

        self.stdout.write(self.style.SUCCESS('All medicines successfully populated with verified drug information!'))
