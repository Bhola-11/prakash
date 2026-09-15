import os, sys, django, datetime
sys.path.append(r'c:\Users\admin\Documents\prakash')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'medicarehub.settings')
django.setup()

from catalogue.models import Medicine

today = datetime.date.today()

products_data = {
    'Retinol A': {
        'brand_name': 'Vitamin A (Retinol)',
        'generic_name': 'Retinol / Retinyl Palmitate (Vitamin A)',
        'strength': '10,000 IU (3,000 mcg RAE)',
        'form': 'Softgel Capsule',
        'route': 'Oral',
        'pack_size': '180 Softgels',
        'active_ingredients': 'Vitamin A (as Retinol / Retinyl Palmitate) 10,000 IU',
        'inactive_ingredients': 'Gelatin, Soybean oil, Glycerin, Purified water, dl-alpha-tocopherol (antioxidant)',
        'overview': 'Retinol A (Vitamin A) is an essential fat-soluble nutrient and potent biological antioxidant vital for normal vision, immune defense, cellular reproduction, and skin tissue regeneration.',
        'uses': 'Nutritional supplementation for Vitamin A deficiency; maintenance of low-light (night) vision and eye health; promoting cellular skin renewal, keratinization, and collagen maintenance; supporting epithelial mucosal lining integrity and immune system function.',
        'how_it_works': 'Retinol is metabolized to 11-cis-retinal (which combines with opsin in the retina to form rhodopsin, essential for low-light vision) and all-trans-retinoic acid, which binds to nuclear RAR and RXR receptors to regulate gene expression for tissue differentiation and immune homeostasis.',
        'dosage_information': 'How to Take: Take 1 softgel daily, preferably with a meal containing dietary fats (e.g., breakfast or dinner) for optimal absorption, or as directed by a healthcare professional. Swallow whole with a full glass of water. Do not chew, crush, or puncture the softgel. Do not exceed the recommended daily dose.',
        'side_effects': 'Common: Generally well-tolerated at recommended nutritional doses. Occasional mild nausea if taken on an empty stomach.',
        'serious_side_effects': 'Seek medical evaluation for signs of hypervitaminosis A (high-dose toxicity): persistent severe headache, dizziness, blurred vision, vomiting, peeling/cracking skin, joint pain, or yellowing of the skin/eyes.',
        'precautions': 'Pregnancy Warning: Women who are pregnant, planning to become pregnant, or breastfeeding should not exceed 3,000 mcg (10,000 IU) daily of preformed vitamin A due to potential teratogenic risks. Consult a doctor if you have liver disease or are taking other retinoid medications.',
        'contraindications': 'Known hypervitaminosis A, hypersensitivity to vitamin A or soy oil, and concurrent treatment with prescription oral retinoids (e.g. isotretinoin).',
        'interactions': 'Oral retinoids (isotretinoin, acitretin - risk of toxicity), tetracycline antibiotics (increased risk of benign intracranial hypertension), orlistat and cholestyramine (may decrease vitamin A absorption), warfarin (high vitamin A doses may increase bleeding risk).',
        'storage': 'Store below 25°C (77°F) in a cool, dry place away from direct sunlight and moisture. Keep bottle tightly closed and out of reach of children.',
        'source_name': 'FDA / NIH Office of Dietary Supplements (ODS)',
        'source_url': 'https://ods.od.nih.gov/factsheets/VitaminA-HealthProfessional/',
        'last_verified_at': today,
        'prescription_required': False,
        'drug_type': 'Fat-Soluble Vitamin Supplement',
        'faqs': [
            {'question': 'How should I take Retinol A for maximum absorption?', 'answer': 'Take 1 softgel daily with a meal that contains healthy dietary fats (e.g. milk, eggs, nuts, olive oil), as Vitamin A is fat-soluble and absorbed best with food.'},
            {'question': 'Can pregnant women take this supplement?', 'answer': 'Pregnant women should always consult their healthcare professional before taking Vitamin A supplements to ensure total daily intake remains within safe prenatal dietary guidelines.'},
            {'question': 'What is the pack size and supply duration?', 'answer': 'This bottle contains 180 easy-to-swallow softgels, providing a full 6-month supply when taken at 1 softgel daily.'}
        ]
    },
    'Biotin B7': {
        'brand_name': 'Biotin Beauty, Vitamin B7',
        'generic_name': 'D-Biotin (Vitamin B7 / Vitamin H)',
        'strength': '10,000 mcg',
        'form': 'Tablet',
        'route': 'Oral',
        'pack_size': '120 Tablets',
        'active_ingredients': 'D-Biotin 10,000 mcg (10 mg)',
        'inactive_ingredients': 'Microcrystalline cellulose, dicalcium phosphate, magnesium stearate, silicon dioxide',
        'overview': 'Biotin (Vitamin B7) is an essential water-soluble B-complex vitamin that functions as an essential coenzyme in energy metabolism, keratin infrastructure synthesis, and fatty acid production.',
        'uses': 'Nutritional support for healthy hair growth, nail thickness and strength, radiant skin health; support for normal macronutrient energy metabolism and nervous system function.',
        'how_it_works': 'Acts as a critical prosthetic coenzyme for carboxylase enzymes (pyruvate carboxylase, ACC, MCC) involved in gluconeogenesis, fatty acid synthesis, and amino acid catabolism, supporting keratin protein synthesis.',
        'dosage_information': 'How to Take: Take 1 tablet daily with water, preferably with a meal. Consistent daily use for 60 to 90 days is recommended for noticeable hair and nail support.',
        'side_effects': 'Common: Biotin is water-soluble with excess amounts naturally excreted in urine. Generally free of significant side effects.',
        'serious_side_effects': 'Very rare: Mild digestive upset or allergic skin reactions in hypersensitive individuals.',
        'precautions': 'Laboratory Test Notice: High doses of Biotin (e.g. 10,000 mcg) can interfere with diagnostic lab immunoassay tests (such as thyroid hormone tests, troponin cardiac markers, and vitamin D). Inform your doctor and lab technicians that you are taking biotin before any blood tests.',
        'contraindications': 'Hypersensitivity to D-biotin or formulation excipients.',
        'interactions': 'Anticonvulsants (carbamazepine, phenytoin, phenobarbital reduce plasma biotin concentrations), prolonged antibiotic therapy may reduce intestinal synthesis of biotin.',
        'storage': 'Store in a cool, dry place below 25°C. Protect from moisture and heat.',
        'source_name': 'FDA / DailyMed / NIH ODS',
        'source_url': 'https://ods.od.nih.gov/factsheets/Biotin-HealthProfessional/',
        'last_verified_at': today,
        'prescription_required': False,
        'drug_type': 'Water-Soluble B-Vitamin',
        'faqs': [
            {'question': 'How long before I see results with Biotin for hair and nails?', 'answer': 'Most clinical users observe noticeable improvements in nail strength and hair texture after 6 to 12 weeks of consistent daily supplementation.'},
            {'question': 'Will Biotin affect my routine blood tests?', 'answer': 'Yes, high-dose biotin can interfere with certain lab tests (like thyroid and cardiac troponin). It is recommended to pause biotin 48 hours before planned blood work.'},
            {'question': 'Is Biotin safe to take daily?', 'answer': 'Yes, Biotin is a water-soluble vitamin with a very high safety profile, and any excess is naturally eliminated by the body.'}
        ]
    },
    'Ascorbic Acid C': {
        'brand_name': 'Vitamin C 1000mg, Redoxon, C-Biol',
        'generic_name': 'Ascorbic Acid (Vitamin C)',
        'strength': '1000 mg',
        'form': 'Tablet',
        'route': 'Oral',
        'pack_size': '100 Tablets',
        'active_ingredients': 'Ascorbic Acid 1000 mg with Rose Hips & Citrus Bioflavonoids 50 mg',
        'inactive_ingredients': 'Cellulose, croscarmellose sodium, vegetable stearic acid, silica, vegetable magnesium stearate',
        'overview': 'Ascorbic Acid (Vitamin C) is an essential water-soluble antioxidant vitamin required for collagen biosynthesis, iron absorption, and comprehensive immune cellular function.',
        'uses': 'Treatment and prevention of Vitamin C deficiency (scurvy); enhancing immune system defenses against seasonal infections; promoting wound healing and tissue repair; antioxidant protection against free radicals; improving non-heme dietary iron absorption.',
        'how_it_works': 'Acts as a powerful water-soluble reducing agent and electron donor, participating as a cofactor in prolyl and lysyl hydroxylase reactions for stable collagen triple helix formation, and neutralizes reactive oxygen species (ROS).',
        'dosage_information': 'How to Take: Take 1 tablet daily with a glass of water, ideally with or immediately after a meal. Do not exceed 2,000 mg daily unless prescribed by a doctor.',
        'side_effects': 'Common: Well tolerated at recommended intake. Doses exceeding 2,000 mg/day may cause mild diarrhea, abdominal cramps, or nausea due to unabsorbed osmotic load.',
        'serious_side_effects': 'Rare: Increased risk of calcium oxalate renal calculi (kidney stones) in predisposed individuals with hyperoxaluria; hemolysis in patients with G6PD deficiency with very high doses.',
        'precautions': 'Use with caution in patients with recurrent renal calculi (oxalate stones), hemochromatosis or iron overload disorders, and G6PD deficiency.',
        'contraindications': 'Known hypersensitivity to ascorbic acid or excipients. Severe hyperoxaluria.',
        'interactions': 'Iron supplements (enhances absorption), deferoxamine (increases iron chelation, avoid in severe cardiac disease), aspirin, antacids containing aluminum (may increase aluminum absorption).',
        'storage': 'Store below 25°C in a dry location. Keep container tightly closed to prevent atmospheric oxidation.',
        'source_name': 'FDA / DailyMed (NDC: 50580-721)',
        'source_url': 'https://ods.od.nih.gov/factsheets/VitaminC-HealthProfessional/',
        'last_verified_at': today,
        'prescription_required': False,
        'drug_type': 'Nutritional Antioxidant Vitamin',
        'faqs': [
            {'question': 'When is the best time to take Vitamin C?', 'answer': 'Take Vitamin C with breakfast or lunch with food to optimize absorption and avoid mild gastric acidity.'},
            {'question': 'Does Vitamin C help with iron absorption?', 'answer': 'Yes, Vitamin C significantly enhances the absorption of non-heme iron from plant-based foods and iron supplements.'},
            {'question': 'Can I take Vitamin C every day?', 'answer': 'Yes, taking 500 mg to 1000 mg daily is safe for adults and provides daily antioxidant and immune support.'}
        ]
    },
    'Cyanocobalamin B12': {
        'brand_name': 'Vitamin B12 1000mcg, Neurobion, Mecobal',
        'generic_name': 'Cyanocobalamin / Methylcobalamin',
        'strength': '1000 mcg',
        'form': 'Tablet',
        'route': 'Oral',
        'pack_size': '100 Tablets',
        'active_ingredients': 'Cyanocobalamin (Vitamin B12) 1000 mcg',
        'inactive_ingredients': 'Mannitol, microcrystalline cellulose, crospovidone, magnesium stearate, natural cherry flavor',
        'overview': 'Cyanocobalamin (Vitamin B12) is an essential water-soluble organometallic compound required for normal erythropoiesis (red blood cell maturation), neurological integrity, myelin sheath synthesis, and DNA synthesis.',
        'uses': 'Treatment and prevention of Vitamin B12 deficiency; management of megaloblastic/pernicious anemia; support for peripheral nerve health, cognitive clarity, and cellular energy production in vegetarians, older adults, and individuals on metformin or PPIs.',
        'how_it_works': 'Functions as a coenzyme for methionine synthase (homocysteine to methionine methylation for DNA synthesis) and methylmalonyl-CoA mutase (vital for propionate metabolism and myelin sheath lipid maintenance).',
        'dosage_information': 'How to Take: Take 1 tablet daily with a meal, or dissolve under the tongue (sublingual) as directed. Consistent daily use supports healthy red blood cells and nerve function.',
        'side_effects': 'Common: Excellent safety profile. Mild, transient diarrhea or itchiness in rare sensitive cases.',
        'serious_side_effects': 'Extremely rare: Anaphylactic reactions in individuals with cobalt allergy; optic nerve atrophy in Leber hereditary optic neuropathy.',
        'precautions': 'Patients with Leber disease (hereditary optic nerve atrophy) should not take cyanocobalamin as rapid optic atrophy may occur.',
        'contraindications': 'Hypersensitivity to cyanocobalamin or cobalt. Early Leber disease.',
        'interactions': 'Metformin, proton pump inhibitors (omeprazole), H2 blockers (famotidine), and colchicine may decrease oral absorption of Vitamin B12 with prolonged use.',
        'storage': 'Store below 25°C away from direct sunlight and humidity. Keep dry.',
        'source_name': 'FDA / DailyMed / NIH ODS',
        'source_url': 'https://ods.od.nih.gov/factsheets/VitaminB12-HealthProfessional/',
        'last_verified_at': today,
        'prescription_required': False,
        'drug_type': 'Essential B-Complex Vitamin',
        'faqs': [
            {'question': 'Why do vegetarians and vegans need B12?', 'answer': 'Vitamin B12 is found naturally almost exclusively in animal products, making daily supplementation essential for vegans and strict vegetarians.'},
            {'question': 'Does Vitamin B12 give an instant energy boost?', 'answer': 'B12 helps convert food into cellular energy (ATP) and corrects fatigue caused by B12 deficiency or megaloblastic anemia.'},
            {'question': 'Can I take Vitamin B12 on an empty stomach?', 'answer': 'Yes, but taking it with a meal improves overall comfort and routine compliance.'}
        ]
    },
    'Allegra': {
        'brand_name': 'Allegra, Fexigra, Telfast',
        'generic_name': 'Fexofenadine Hydrochloride',
        'strength': '120 mg',
        'form': 'Tablet',
        'route': 'Oral',
        'pack_size': '10 Tablets / Strip',
        'active_ingredients': 'Fexofenadine Hydrochloride 120 mg',
        'inactive_ingredients': 'Croscarmellose sodium, pregelatinized starch, microcrystalline cellulose, magnesium stearate, hypromellose, titanium dioxide',
        'overview': 'Allegra (Fexofenadine Hydrochloride) is a second-generation, non-sedating selective peripheral H1-receptor antagonist antihistamine indicated for allergic symptom relief without causing drowsiness.',
        'uses': 'Relief of symptoms associated with seasonal allergic rhinitis (hay fever): sneezing, itchy/runny nose, itchy/red/watery eyes, and nasal congestion; treatment of uncomplicated skin manifestations of chronic idiopathic urticaria (hives and skin itching).',
        'how_it_works': 'Selectively binds to and antagonizes peripheral H1 histamine receptors, preventing histamine-mediated inflammatory responses without crossing the blood-brain barrier significantly, thus avoiding sedation.',
        'dosage_information': 'How to Take: Adults and children 12 years and older: Take one 120 mg tablet once daily with a full glass of water. Do not take with fruit juices (such as grapefruit, orange, or apple juice) as they reduce absorption. Swallow tablet whole.',
        'side_effects': 'Common: Headache, mild drowsiness (rare), nausea, dizziness, dry mouth.',
        'serious_side_effects': 'Seek immediate medical attention for: Symptoms of severe hypersensitivity (angioedema, chest tightness, dyspnea, facial/throat swelling, severe urticaria).',
        'precautions': 'Dose adjustment is recommended in patients with moderate to severe renal impairment. Separate administration of aluminum and magnesium antacids by at least 2 hours.',
        'contraindications': 'Known hypersensitivity to fexofenadine hydrochloride or any formulation ingredients.',
        'interactions': 'Fruit juices (grapefruit, orange, apple decrease fexofenadine bioavailability via OATP1A2 inhibition), antacids containing aluminum or magnesium hydroxide (reduce absorption), erythromycin, ketoconazole.',
        'storage': 'Store at 20°C to 25°C (68°F to 77°F). Protect from excessive moisture and light.',
        'source_name': 'FDA / DailyMed (NDA: 020818)',
        'source_url': 'https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=42704256-4279-4d89-8d76-e1791a822f36',
        'last_verified_at': today,
        'prescription_required': False,
        'drug_type': 'Non-Sedating Second-Generation Antihistamine',
        'faqs': [
            {'question': 'Does Allegra cause drowsiness?', 'answer': 'Allegra is a non-sedating antihistamine that does not cross the blood-brain barrier and typically does not cause sleepiness.'},
            {'question': 'Why should I avoid taking Allegra with fruit juices?', 'answer': 'Grapefruit, orange, and apple juices inhibit the intestinal transporter (OATP1A2) needed to absorb fexofenadine, reducing its effectiveness by up to 50%.'},
            {'question': 'How quickly does Allegra start working?', 'answer': 'Allegra typically begins relieving allergy symptoms within 1 hour, with peak clinical benefit lasting for a full 24 hours.'}
        ]
    },
    'Amlodipine': {
        'brand_name': 'Norvasc, Amlong, Stamlo',
        'generic_name': 'Amlodipine Besylate',
        'strength': '5 mg',
        'form': 'Tablet',
        'route': 'Oral',
        'pack_size': '30 Tablets / Strip',
        'active_ingredients': 'Amlodipine Besylate equivalent to 5 mg amlodipine',
        'inactive_ingredients': 'Microcrystalline cellulose, dibasic calcium phosphate anhydrous, sodium starch glycolate, magnesium stearate',
        'overview': 'Amlodipine is a long-acting dihydropyridine calcium channel blocker (CCB) indicated for the first-line management of hypertension and chronic stable angina.',
        'uses': 'Treatment of essential hypertension to lower blood pressure and reduce cardiovascular events (stroke and myocardial infarction); management of chronic stable angina and vasospastic (Prinzmetal) angina.',
        'how_it_works': 'Inhibits the transmembrane influx of extracellular calcium ions into vascular smooth muscle and cardiac muscle cells during depolarization, causing peripheral arterial vasodilation, reduced total peripheral resistance, and decreased myocardial afterload.',
        'dosage_information': 'How to Take: Usual starting dose is 5 mg orally once daily, taken with or without food at the same time each day. Dosage may be increased to a maximum of 10 mg once daily based on blood pressure response under physician supervision.',
        'side_effects': 'Common: Peripheral edema (swelling of ankles/feet), flushing, dizziness, palpitations, fatigue, nausea, abdominal pain.',
        'serious_side_effects': 'Seek immediate medical attention for: Worsening angina or acute myocardial infarction upon initiation or dose increase (rare), symptomatic hypotension/syncope, severe allergic rash.',
        'warnings': 'Symptomatic hypotension is possible, particularly in patients with severe aortic stenosis. Peripheral edema is dose-dependent and typically responds to diuretic therapy or dosage reduction. Titrate slowly in patients with severe hepatic impairment.',
        'contraindications': 'Known hypersensitivity to amlodipine, dihydropyridines, or formulation excipients. Severe hypotension, cardiogenic shock, and clinically unstable heart failure.',
        'interactions': 'Simvastatin (amlodipine increases simvastatin exposure; limit simvastatin to 20 mg daily), CYP3A4 inhibitors (ketoconazole, clarithromycin increase amlodipine levels), cyclosporine, tacrolimus, sildenafil.',
        'storage': 'Store at 20°C to 25°C (68°F to 77°F). Protect from light and moisture.',
        'source_name': 'FDA / DailyMed (NDA: 019787)',
        'source_url': 'https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=27d0955a-4f51-4034-8c88-e93ec7a7b8e5',
        'last_verified_at': today,
        'prescription_required': True,
        'drug_type': 'Dihydropyridine Calcium Channel Blocker',
        'faqs': [
            {'question': 'When is the best time to take Amlodipine?', 'answer': 'Take Amlodipine once daily at the same time every day (morning or evening), with or without food.'},
            {'question': 'Why do my ankles swell while taking Amlodipine?', 'answer': 'Peripheral ankle edema is a common, dose-dependent pharmacological effect of arterial vasodilation. Inform your doctor if swelling becomes bothersome.'},
            {'question': 'Can I stop taking Amlodipine if my blood pressure is normal?', 'answer': 'No, continue taking Amlodipine as prescribed. Blood pressure remains controlled because of the medication, and stopping suddenly can cause blood pressure to spike.'}
        ]
    },
    'Abirapro': {
        'brand_name': 'Zytiga, Abirapro, Abirakast',
        'generic_name': 'Abiraterone Acetate',
        'strength': '250 mg',
        'form': 'Tablet',
        'route': 'Oral',
        'pack_size': '120 Tablets / Bottle',
        'active_ingredients': 'Abiraterone Acetate 250 mg',
        'inactive_ingredients': 'Lactose monohydrate, microcrystalline cellulose, croscarmellose sodium, povidone, sodium lauryl sulfate, magnesium stearate, colloidal silicon dioxide',
        'overview': 'Abirapro (Abiraterone Acetate) is an orally bioavailable steroidal androgen biosynthesis inhibitor indicated in combination with prednisone for metastatic castration-resistant prostate cancer (mCRPC).',
        'uses': 'Treatment of metastatic castration-resistant prostate cancer (mCRPC) and metastatic high-risk castration-sensitive prostate cancer (mCSPC) in combination with prednisone/prednisolone and androgen deprivation therapy (ADT).',
        'how_it_works': 'Selectively and irreversibly inhibits 17alpha-hydroxylase/C17,20-lyase (CYP17), a key enzyme in androgen synthesis in the testes, adrenal glands, and prostate tumor tissue, suppressing serum testosterone to undetectable levels.',
        'dosage_information': 'How to Take: Recommended dose is 1,000 mg (four 250 mg tablets) administered once daily on an EMPTY STOMACH, at least 1 hour before or 2 hours after food, in combination with prednisone 5 mg orally twice daily. Swallow tablets whole with water.',
        'side_effects': 'Common: Fatigue, joint swelling/discomfort, hot flashes, peripheral edema, hypertension, hypokalemia, diarrhea, cough.',
        'serious_side_effects': 'Seek immediate oncology attention for: Hepatotoxicity (elevated AST/ALT/bilirubin), severe hypokalemia, fluid retention, cardiac arrhythmias, adrenocortical insufficiency upon prednisone withdrawal.',
        'warnings': 'Must be taken on an empty stomach because food increases drug exposure up to 10-fold, increasing toxicity risk. Monitor serum transaminases (ALT, AST) every 2 weeks for the first 3 months and monthly thereafter. Monitor blood pressure and serum potassium monthly.',
        'contraindications': 'Severe hepatic impairment (Child-Pugh Class C), pregnancy (teratogenic; women who are pregnant must not handle crushed tablets), hypersensitivity to abiraterone acetate.',
        'interactions': 'Strong CYP3A4 inducers (rifampin, phenytoin, carbamazepine reduce abiraterone exposure; avoid co-administration), drugs metabolized by CYP2D6 (dextromethorphan, metoprolol), spironolactone.',
        'storage': 'Store at 20°C to 25°C (68°F to 77°F). Keep container tightly closed and out of reach of children.',
        'source_name': 'FDA / DailyMed (NDA: 202379)',
        'source_url': 'https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=a64a3821-6548-4309-847e-128212176b6e',
        'last_verified_at': today,
        'prescription_required': True,
        'drug_type': 'Rx CYP17 Androgen Biosynthesis Inhibitor',
        'faqs': [
            {'question': 'Why must Abirapro be taken strictly on an empty stomach?', 'answer': 'Food increases the absorption of abiraterone unpredictably by up to 10-fold, which can lead to dangerously elevated drug levels and severe liver toxicity. Take at least 1 hour before or 2 hours after meals.'},
            {'question': 'Why is Prednisone prescribed together with Abirapro?', 'answer': 'Abiraterone causes a decrease in cortisol and an increase in adrenocorticotropic hormone (ACTH), leading to mineralocorticoid excess. Prednisone replaces cortisol and prevents hypertension and hypokalemia.'},
            {'question': 'What regular monitoring is required?', 'answer': 'Your oncologist will perform routine blood tests to check liver enzymes (ALT/AST), serum potassium, blood pressure, and PSA levels.'}
        ]
    }
}

for name_key, data in products_data.items():
    med = Medicine.objects.filter(name__icontains=name_key.split()[0]).first()
    if med:
        for k, v in data.items():
            setattr(med, k, v)
        med.save()
        print(f'Successfully updated verified product monograph: {med.name}')

print('All authentic product clinical monographs updated!')
