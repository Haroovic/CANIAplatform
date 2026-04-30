"""
CANIA Database Seed Script
Run this script ONCE to populate the database with 30 Expert Q&As.
This will reset the database to ensure the schema is correct.
Usage: python seed_database.py
"""
from main import app, db
from models import Question
from datetime import datetime
def seed_questions():
    qas = [
        {
            "question": "What foods should I eat to support my lungs during cancer treatment?",
            "keywords": "diet, food, nutrition, eating, meals, healthy",
            "answer": "Focus on a nutrient-rich diet including fruits and vegetables high in antioxidants (berries, leafy greens, tomatoes), lean proteins (fish, chicken, beans) to maintain muscle mass, whole grains for sustained energy, and healthy fats from nuts and olive oil. Stay hydrated with water and herbal teas. Small, frequent meals can help if you experience nausea or loss of appetite during treatment."
        },
        {
            "question": "Is it safe to exercise if I have lung cancer?",
            "keywords": "exercise, physical activity, workout, fitness, movement, sport",
            "answer": "Yes, moderate exercise is generally beneficial and safe for most lung cancer patients. Activities like walking, gentle yoga, and light strength training can help maintain stamina, reduce fatigue, improve mood, and enhance overall quality of life. Always consult your oncologist before starting any exercise program, and listen to your body. Start slowly and gradually increase intensity as tolerated."
        },
        {
            "question": "How much sleep do I need during cancer treatment?",
            "keywords": "sleep, rest, fatigue, tired, energy, sleeping",
            "answer": "Aim for 7-9 hours of quality sleep per night, and don't hesitate to take short naps (20-30 minutes) during the day if needed. Cancer treatment can cause significant fatigue, so your body needs extra rest to heal. Establish a consistent sleep schedule, create a comfortable sleep environment, avoid caffeine late in the day, and practice relaxation techniques before bed to improve sleep quality."
        },
        {
            "question": "What are the early warning signs of lung cancer?",
            "keywords": "symptoms, signs, warning, early, detect, diagnosis",
            "answer": "Early lung cancer may have no symptoms, which is why screening is important for high-risk individuals. When symptoms do appear, they may include: persistent cough that worsens over time, coughing up blood, chest pain that worsens with deep breathing, unexplained weight loss, shortness of breath, recurrent respiratory infections, hoarseness, and fatigue. If you experience any of these symptoms, especially if you're a current or former smoker, consult your doctor promptly."
        },
        {
            "question": "Can I continue working during lung cancer treatment?",
            "keywords": "work, job, employment, career, working, productivity",
            "answer": "Many lung cancer patients continue working during treatment, though this depends on your specific situation, treatment type, and how you feel. Some people work full-time, others reduce hours, and some take medical leave. Communicate openly with your employer about your needs. Consider flexible schedules or remote work options. Prioritize rest and don't push yourself too hard. It's okay to take time off if needed—your health comes first."
        },
        {
            "question": "What breathing exercises can help with shortness of breath?",
            "keywords": "breathing, breathe, respiratory, oxygen, air, lungs",
            "answer": "Several techniques can help: Pursed-lip breathing (inhale through nose, exhale slowly through pursed lips), diaphragmatic breathing (belly breathing), and the 4-7-8 technique (inhale for 4 counts, hold for 7, exhale for 8). Practice these exercises daily when you're feeling well, so they're easier to use during episodes of breathlessness. A pulmonary rehabilitation program can teach you additional techniques tailored to your specific needs."
        },
        {
            "question": "How can I manage cancer-related pain without medication?",
            "keywords": "pain, discomfort, hurt, ache, relief, manage",
            "answer": "Complementary approaches include: heat or cold therapy, gentle massage, acupuncture, meditation and mindfulness, guided imagery, progressive muscle relaxation, and distraction techniques (music, art, reading). While these methods can be very helpful, don't suffer unnecessarily—discuss pain management with your healthcare team. A combination of medication and non-medication approaches often works best."
        },
        {
            "question": "Should I avoid certain foods during chemotherapy?",
            "keywords": "chemotherapy, chemo, treatment, avoid, food, diet",
            "answer": "During chemotherapy, avoid: raw or undercooked foods (sushi, rare meat, raw eggs) due to infection risk, unwashed fruits and vegetables, unpasteurized dairy products, excessive alcohol, and foods that worsen nausea for you personally. Focus on well-cooked foods, wash all produce thoroughly, and eat smaller, more frequent meals. Stay hydrated and maintain good food safety practices at home."
        },
        {
            "question": "Can stress make my lung cancer worse?",
            "keywords": "stress, anxiety, mental health, emotional, worry, depression",
            "answer": "While stress doesn't directly cause or worsen cancer growth, chronic stress can weaken your immune system, interfere with treatment adherence, and reduce quality of life. Managing stress is important for overall well-being. Helpful strategies include: counseling or therapy, support groups, meditation, gentle exercise, spending time with loved ones, engaging in hobbies, and possibly medication for anxiety or depression if recommended by your doctor."
        },
        {
            "question": "What supplements should I take with lung cancer?",
            "keywords": "supplements, vitamins, minerals, herbs, natural, alternative",
            "answer": "NEVER take supplements without discussing them with your oncologist first. Some supplements can interfere with cancer treatments or have harmful effects. Your doctor may recommend specific vitamins if you have documented deficiencies (like vitamin D, B12). Focus on getting nutrients from whole foods when possible. If your doctor approves supplements, choose reputable brands and disclose all supplements you're taking to your entire healthcare team."
        },
        {
            "question": "How often should I get screened for lung cancer recurrence?",
            "keywords": "screening, scan, test, checkup, monitoring, follow-up",
            "answer": "Follow-up schedules vary based on your cancer stage and treatment, but typically include: CT scans every 6-12 months for the first 2-3 years, then annually; regular physical exams every 3-6 months initially, then less frequently; and ongoing symptom monitoring. Your oncologist will create a personalized surveillance plan. Always report new or worsening symptoms between scheduled appointments. Early detection of recurrence improves treatment options."
        },
        {
            "question": "Is secondhand smoke dangerous for lung cancer patients?",
            "keywords": "smoke, smoking, tobacco, cigarettes, secondhand, exposure",
            "answer": "Yes, secondhand smoke is harmful for everyone, especially lung cancer patients. It can worsen respiratory symptoms, interfere with treatment effectiveness, and increase risk of recurrence. Avoid all tobacco smoke exposure. Ask family and visitors not to smoke around you or in your home/car. If you're still smoking, quitting is the single most important thing you can do for your health—talk to your doctor about cessation programs and support."
        },
        {
            "question": "Can I travel during lung cancer treatment?",
            "keywords": "travel, trip, vacation, flying, airplane, journey",
            "answer": "Travel is often possible, but requires planning and your doctor's approval. Consider: timing (avoid travel during intense treatment phases), destination (stay near quality medical facilities), oxygen needs for flights, infection risk in crowds, travel insurance, carrying medications and medical records, and having a plan for emergencies. Short trips may be easier than extended travel. Some people find travel energizing and mood-lifting when timed appropriately."
        },
        {
            "question": "What are the side effects of radiation therapy for lung cancer?",
            "keywords": "radiation, radiotherapy, side effects, treatment, therapy",
            "answer": "Common side effects include: fatigue (often worsening throughout treatment), skin changes in the treated area (redness, sensitivity), difficulty swallowing if esophagus is in the radiation field, shortness of breath, cough, and chest discomfort. Most side effects are temporary and improve after treatment ends. Use gentle skin care products, stay hydrated, rest when needed, and report severe symptoms promptly. Long-term effects may include lung scarring or heart issues, which your team will monitor."
        },
        {
            "question": "How can I boost my immune system during cancer treatment?",
            "keywords": "immune system, immunity, defense, infection, prevention, health",
            "answer": "Support your immune system by: getting adequate sleep, eating a balanced diet rich in fruits and vegetables, staying hydrated, managing stress, washing hands frequently, avoiding sick people and crowds when your counts are low, keeping vaccinations up to date (check with your doctor first), exercising moderately, and not smoking. Some treatments temporarily weaken immunity, so take extra precautions during those times. Report any fever or signs of infection immediately."
        },
        {
            "question": "What is the survival rate for lung cancer?",
            "keywords": "survival, prognosis, outlook, statistics, cure, life expectancy",
            "answer": "Survival rates vary greatly depending on cancer type, stage at diagnosis, and treatment response. Early-stage lung cancer has much better outcomes than advanced disease. Recent advances in targeted therapy and immunotherapy have significantly improved survival for many patients. Your individual prognosis depends on YOUR specific situation—not statistics. Focus on working with your healthcare team, following your treatment plan, and maintaining the best quality of life possible. Many people live for years with lung cancer."
        },
        {
            "question": "Should I join a support group for lung cancer patients?",
            "keywords": "support group, community, help, emotional support, others, patients",
            "answer": "Support groups can be incredibly valuable, providing: emotional support from people who truly understand, practical tips from others' experiences, reduced feelings of isolation, a safe space to express fears and concerns, and information about resources. Groups may meet in-person or online. Try a few different groups to find the right fit. Some people also benefit from one-on-one counseling. There's no pressure—use whatever support feels right for you."
        },
        {
            "question": "Can I drink alcohol while undergoing lung cancer treatment?",
            "keywords": "alcohol, drinking, beer, wine, spirits, beverages",
            "answer": "This depends on your specific treatment and overall health. Generally, moderate alcohol consumption (if approved by your doctor) may be okay, but many patients are advised to avoid or minimize alcohol because it can: interfere with some medications, worsen side effects like nausea, dehydrate you, suppress immune function, and interact with liver function. Always ask your oncologist about alcohol consumption with your specific treatment regimen. When in doubt, it's safer to abstain."
        },
        {
            "question": "What questions should I ask my oncologist at appointments?",
            "keywords": "questions, doctor, oncologist, appointment, ask, communication",
            "answer": "Important questions include: What is my exact diagnosis and stage? What are my treatment options and their pros/cons? What are the goals of treatment? What side effects should I expect? How will we monitor treatment effectiveness? What clinical trials am I eligible for? When should I call between appointments? What lifestyle changes should I make? Can you recommend resources or support services? Don't hesitate to ask for clarification or bring a list of questions to each appointment."
        },
        {
            "question": "How can I cope with the emotional impact of a lung cancer diagnosis?",
            "keywords": "emotional, coping, feelings, scared, overwhelmed, mental, psychological",
            "answer": "It's normal to experience a range of emotions: fear, anger, sadness, anxiety. Healthy coping strategies include: acknowledging your feelings, talking to loved ones or a therapist, joining a support group, practicing mindfulness or meditation, maintaining routines when possible, staying informed about your treatment, setting small achievable goals, engaging in activities you enjoy, and accepting help from others. Professional counseling can be especially helpful for managing cancer-related distress."
        },
        {
            "question": "What are the benefits of immunotherapy for lung cancer?",
            "keywords": "immunotherapy, treatment, therapy, immune, checkpoint inhibitors",
            "answer": "Immunotherapy helps your immune system recognize and attack cancer cells. Benefits may include: durable responses (long-lasting effects), potentially fewer side effects than traditional chemotherapy, effectiveness for some cancers that don't respond well to other treatments, and possible combination with other therapies. Not all lung cancers respond to immunotherapy—biomarker testing helps determine if it's right for you. Side effects differ from chemotherapy and require specific monitoring and management."
        },
        {
            "question": "Can lung cancer spread to other parts of the body?",
            "keywords": "metastasis, spread, metastatic, stage 4, advanced, other organs",
            "answer": "Yes, lung cancer can metastasize (spread) to other organs, commonly the brain, bones, liver, and adrenal glands. This is called metastatic or stage IV lung cancer. Symptoms depend on where it spreads. Regular scans help detect metastases early. Even when cancer has spread, treatments are available that can control the disease, relieve symptoms, and extend life. Never lose hope—treatment advances continue to improve outcomes for metastatic lung cancer."
        },
        {
            "question": "What is targeted therapy and how does it work?",
            "keywords": "targeted therapy, precision medicine, mutations, EGFR, ALK, treatment",
            "answer": "Targeted therapy uses drugs that specifically target genetic mutations or proteins in cancer cells, causing less harm to normal cells than traditional chemotherapy. Your tumor will be tested for specific mutations (like EGFR, ALK, ROS1). If you have a targetable mutation, these therapies can be very effective, often with manageable side effects. They're usually taken as daily pills. Not all lung cancers have targetable mutations, but testing is standard practice to identify the best treatment approach for you."
        },
        {
            "question": "How can I manage nausea and vomiting from chemotherapy?",
            "keywords": "nausea, vomiting, sick, upset stomach, anti-nausea, chemotherapy",
            "answer": "Strategies include: taking anti-nausea medications as prescribed (don't wait until you feel sick), eating small frequent meals, avoiding strong smells and greasy or spicy foods, trying ginger tea or candies, staying hydrated with small sips throughout the day, eating bland foods (crackers, toast, rice), trying acupressure wristbands, and keeping your environment cool and well-ventilated. If nausea is severe or persistent, contact your healthcare team—they can adjust your medications to better control symptoms."
        },
        {
            "question": "What is palliative care and when should I consider it?",
            "keywords": "palliative care, hospice, end of life, comfort, quality of life",
            "answer": "Palliative care focuses on improving quality of life and managing symptoms at any stage of serious illness—you don't have to be at end of life to benefit. It can be provided alongside curative treatment and addresses pain, fatigue, breathing problems, anxiety, and other concerns. Palliative care specialists work with your oncology team to optimize your comfort and functioning. Consider it if you're experiencing difficult symptoms or need extra support. It's different from hospice, which is specifically for end-of-life care."
        },
        {
            "question": "Can I use marijuana/cannabis during cancer treatment?",
            "keywords": "marijuana, cannabis, CBD, medical marijuana, THC, weed",
            "answer": "Medical cannabis is legal in some areas and may help with symptoms like pain, nausea, and appetite loss. However, you MUST discuss this with your oncologist first because: it can interact with some cancer treatments, smoking anything is harmful to lungs, quality and dosing vary widely, and it may not be legal in your location. If approved, your doctor can guide you toward regulated products and appropriate dosing. Never stop prescribed medications in favor of cannabis without medical supervision."
        },
        {
            "question": "How do I know if my treatment is working?",
            "keywords": "treatment response, effectiveness, working, scan results, progress",
            "answer": "Treatment effectiveness is monitored through: regular imaging scans (CT, PET) comparing tumor size over time, blood tests for tumor markers, physical exams, and symptom assessment. Your doctor will discuss scan results with you, using terms like 'complete response,' 'partial response,' 'stable disease,' or 'progression.' Improvement may be gradual. Sometimes scans show initial apparent worsening (pseudoprogression) before improvement. Ask your doctor to explain your results and what they mean for your treatment plan."
        },
        {
            "question": "What should I keep in my cancer care emergency kit at home?",
            "keywords": "emergency, prepare, kit, supplies, home, medications",
            "answer": "Essential items include: updated medication list with dosages, emergency contact numbers (oncologist, hospital), thermometer, anti-nausea medications, pain relievers approved by your doctor, extra prescription medications, medical records and treatment summary, insurance information, comfortable clothing, water bottle, healthy snacks, and items for comfort (books, music, blankets). Keep a bag ready for unexpected hospital visits. Know when to call your doctor vs. going to the emergency room, and have transportation arranged for emergencies."
        },
        {
            "question": "Is it normal to feel tired all the time during treatment?",
            "keywords": "fatigue, tired, exhausted, energy, weakness, tiredness",
            "answer": "Yes, cancer-related fatigue is extremely common and different from ordinary tiredness. It doesn't improve with rest alone and can be caused by: the cancer itself, treatment effects, anemia, poor nutrition, pain, stress, or sleep problems. Management strategies include: pacing activities, prioritizing important tasks, taking short naps, gentle exercise, eating well, staying hydrated, treating underlying causes (like anemia), and asking for help with daily tasks. Report severe or worsening fatigue to your healthcare team."
        },
        {
            "question": "Can complementary therapies help alongside conventional treatment?",
            "keywords": "complementary, alternative, holistic, integrative, acupuncture, massage",
            "answer": "Complementary therapies used ALONGSIDE (not instead of) conventional treatment can improve quality of life. Beneficial approaches may include: acupuncture for pain and nausea, massage therapy (with oncologist approval), meditation and mindfulness, yoga (gentle forms), music or art therapy, and aromatherapy. Always inform your oncologist about any complementary therapies you're using. Avoid 'alternative' treatments that claim to cure cancer or suggest stopping proven medical treatments—these can be dangerous and waste precious time and resources."
        }
    ]
    with app.app_context():
        print("🛠️  Resetting database to ensure schema matches models...")
        db.drop_all()
        db.create_all()
        print(f"🌱 Seeding database with {len(qas)} expert-created Q&As...")
        added_count = 0
        for qa_data in qas:
            try:
                question = Question(
                    question_text=qa_data["question"],
                    keywords=qa_data["keywords"],
                    answer_text=qa_data["answer"],
                    is_answered=True,
                    is_expert_created=True,
                    date_posted=datetime.utcnow(),
                    date_answered=datetime.utcnow()
                )
                db.session.add(question)
                added_count += 1
            except Exception as e:
                print(f"❌ Error adding question: {e}")
                db.session.rollback()
        db.session.commit()
        print(f"✅ Successfully added {added_count} Q&As to the database!")
        print(f"📊 Final Check: {Question.query.filter_by(is_expert_created=True).count()} total expert items.")
if __name__ == "__main__":
    seed_questions()
