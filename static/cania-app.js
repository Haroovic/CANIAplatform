const TRANSLATIONS = {
  en: {
    'nav.about':'About','nav.help':'Help','nav.signin':'Sign In',
    'nav.join':'Join CANIA','nav.logout':'Log Out','nav.notifications':'Notifications',
    'nav.space':'CANIA Space','nav.scanner':'Scanner','nav.journey':'My Journey',
    'nav.dashboard':'Dashboard','nav.expert':'Expert Dashboard',
    'home.badge':'Advanced Diagnostic Intelligence',
    'home.h1':'Lung Cancer Risk\nDetection',
    'home.lead':'Introducing <strong>CANIA</strong> (<strong>Can</strong>cer <strong>AI</strong>), our state-of-the-art <strong>neural engine</strong> designed to empower patients and clinicians with <strong>instant, AI-driven chest X-ray analysis</strong>. By leveraging advanced <strong>deep learning</strong>, CANIA provides comprehensive screening reports in seconds, facilitating <strong>early detection</strong> and informed clinical <strong>decision-making</strong>.',
    'home.cta':'Get Started',
    'home.how.title':'How It Works',
    'home.how.sub':'A precise medical screening process designed for clarity and safety.',
    'home.how.video':'Watch the Tutorial',
    'home.how.s1':'Securely upload your chest X-ray in JPG or PNG format.',
    'home.how.s2':'Wait for our AI model to process patterns and anomalies.',
    'home.how.s3':'Receive your preliminary report.',
    'home.how.s4':'Consult with a medical specialist to review your AI findings.',
    'home.how.btn':'Start Diagnostic Analysis Now',
    'home.feat.title':'What We Offer',
    'home.feat.sub':'From AI scanning to expert consultation, CANIA covers the full clinical journey.',
    'home.feat.ai.h':'AI X-Ray Analysis','home.feat.ai.p':'Upload your chest X-ray and receive an AI risk assessment in seconds.',
    'home.feat.qa.h':'Expert Q&A Space','home.feat.qa.p':'Ask certified medical professionals and browse our searchable knowledge base.',
    'home.feat.log.h':'Diagnostic Journey Log','home.feat.log.p':'Track every scan in a visual timeline to monitor progress over time.',
    'auth.login.h':'Welcome Back','auth.login.sub':'Please sign in to access your account',
    'auth.login.btn':'Sign In','auth.login.forgot':'Forgot password?','auth.login.new':'New here?',
    'auth.login.create':'Create Account',
    'auth.reg.h':'Create Your Account','auth.reg.sub':'Join us today and get started',
    'auth.reg.btn':'Sign Up','auth.reg.already':'Already have an account?','auth.reg.login':'Log In',
    'dash.welcome':'Welcome back,','dash.sub':'Track your health progress and expert consultations.',
    'dash.scans':'Diagnostic Scans','dash.consult':'Expert Consultations','dash.answered':'Answered',
    'dash.history':'Your Consultation History','dash.date':'Date Submitted','dash.question':'Question',
    'dash.status':'Status','dash.action':'Action','dash.empty':'You haven\'t asked any questions yet.',
    'dash.view':'View Answer','dash.waiting':'Waiting',
    'status.answered':'Answered','status.pending':'Pending',
    'footer.connect':'Connect With Us','footer.support':'Clinical Support',
    'footer.copy':'© 2026 CANIA Neural Systems · Internal Diagnostic Interface',
    'scan.title':'Lung Cancer Risk Detection','scan.sub':'AI-Driven X-Ray Image Analysis',
    'scan.drop':'Click or drag & drop your chest X-Ray','scan.hint':'Supports JPG, PNG',
    'scan.btn':'Execute Risk Detection Scan','scan.loading':'Analysing Neural Networks…',
    'scan.high.title':'Attention: High Risk Patterns Detected',
    'scan.low.title':'Clear: Low Risk Patterns',
    'notif.title':'Notifications','notif.sub':'Stay updated with your CANIA activity',
    'notif.empty':'No Notifications Yet','notif.all':'You\'re all caught up!',
    'journey.title':'My Diagnostic Journey','journey.sub':'Your complete AI scan history',
    'journey.empty':'No Scans Yet','journey.start':'Start First Scan',
  },
  fr: {
    'nav.about':'À propos','nav.help':'Aide','nav.signin':'Se connecter',
    'nav.join':'Rejoindre CANIA','nav.logout':'Se déconnecter','nav.notifications':'Notifications',
    'nav.space':'Espace CANIA','nav.scanner':'Scanner','nav.journey':'Mon Parcours',
    'nav.dashboard':'Tableau de bord','nav.expert':'Tableau Expert',
    'home.badge':'Intelligence Diagnostique Avancée',
    'home.h1':'Détection du Risque\nde Cancer Pulmonaire',
    'home.lead':'Découvrez <strong>CANIA</strong> (<strong>Can</strong>cer <strong>AI</strong>), notre <strong>moteur neuronal</strong> de pointe conçu pour offrir aux patients et aux cliniciens une <strong>analyse radiologique instantanée basée sur l\'IA</strong>. Grâce au <strong>deep learning</strong>, CANIA fournit des rapports de dépistage complets en quelques secondes, facilitant la <strong>détection précoce</strong> et la <strong>prise de décision clinique</strong>.',
    'home.cta':'Commencer',
    'home.how.title':'Comment ça marche','home.how.sub':'Un processus de dépistage médical précis conçu pour la clarté et la sécurité.',
    'home.how.video':'Regarder le tutoriel',
    'home.how.s1':'Téléchargez votre radiographie thoracique en JPG ou PNG.',
    'home.how.s2':'Notre modèle IA analyse les patterns et anomalies.',
    'home.how.s3':'Recevez votre rapport préliminaire.',
    'home.how.s4':'Consultez un spécialiste pour examiner les résultats IA.',
    'home.how.btn':'Démarrer l\'analyse diagnostique',
    'home.feat.title':'Ce que nous offrons','home.feat.sub':'De l\'IA au conseil expert, CANIA couvre tout le parcours clinique.',
    'home.feat.ai.h':'Analyse IA des Radios','home.feat.ai.p':'Téléchargez votre radio et recevez une évaluation du risque en quelques secondes.',
    'home.feat.qa.h':'Espace Q&R Expert','home.feat.qa.p':'Posez des questions à des professionnels médicaux certifiés.',
    'home.feat.log.h':'Journal Diagnostique','home.feat.log.p':'Suivez chaque scan dans une chronologie visuelle.',
    'auth.login.h':'Bon Retour','auth.login.sub':'Connectez-vous pour accéder à votre compte',
    'auth.login.btn':'Se connecter','auth.login.forgot':'Mot de passe oublié ?','auth.login.new':'Nouveau ici ?',
    'auth.login.create':'Créer un compte',
    'auth.reg.h':'Créer votre compte','auth.reg.sub':'Rejoignez-nous aujourd\'hui',
    'auth.reg.btn':'S\'inscrire','auth.reg.already':'Déjà inscrit ?','auth.reg.login':'Se connecter',
    'dash.welcome':'Bon retour,','dash.sub':'Suivez votre progression santé et vos consultations.',
    'dash.scans':'Scans Diagnostiques','dash.consult':'Consultations Expertes','dash.answered':'Répondues',
    'dash.history':'Historique des Consultations','dash.date':'Date','dash.question':'Question',
    'dash.status':'Statut','dash.action':'Action','dash.empty':'Vous n\'avez pas encore posé de questions.',
    'dash.view':'Voir la réponse','dash.waiting':'En attente',
    'status.answered':'Répondu','status.pending':'En attente',
    'footer.connect':'Nous rejoindre','footer.support':'Support Clinique',
    'footer.copy':'© 2026 CANIA Neural Systems · Interface Diagnostique Interne',
    'scan.title':'Détection du Risque de Cancer Pulmonaire','scan.sub':'Analyse IA des Radiographies',
    'scan.drop':'Cliquez ou glissez votre radio thoracique','scan.hint':'JPG, PNG acceptés',
    'scan.btn':'Lancer la détection','scan.loading':'Analyse des réseaux neuronaux…',
    'scan.high.title':'Attention : Patterns à Haut Risque Détectés','scan.low.title':'Clair : Patterns à Faible Risque',
    'notif.title':'Notifications','notif.sub':'Restez informé de votre activité CANIA',
    'notif.empty':'Aucune notification','notif.all':'Vous êtes à jour !',
    'journey.title':'Mon Parcours Diagnostique','journey.sub':'Historique complet de vos scans IA',
    'journey.empty':'Aucun scan encore','journey.start':'Premier Scan',
  },
  ar: {
    'nav.about':'حول','nav.help':'المساعدة','nav.signin':'تسجيل الدخول',
    'nav.join':'انضم إلى كانيا','nav.logout':'تسجيل الخروج','nav.notifications':'الإشعارات',
    'nav.space':'فضاء كانيا','nav.scanner':'الفاحص','nav.journey':'رحلتي',
    'nav.dashboard':'لوحة التحكم','nav.expert':'لوحة الخبراء',
    'home.badge':'ذكاء تشخيصي متقدم',
    'home.h1':'الكشف عن مخاطر\nسرطان الرئة',
    'home.lead':'نُقدّم لكم <strong>كانيا</strong> (<strong>CANIA</strong>)، محركنا العصبي المتطور المصمم لتمكين المرضى والأطباء من <strong>تحليل فوري لصور الأشعة السينية بالذكاء الاصطناعي</strong>. بالاستفادة من <strong>التعلم العميق</strong>، يوفر كانيا تقارير فحص شاملة في ثوانٍ، مما يسهّل <strong>الاكتشاف المبكر</strong> واتخاذ <strong>القرار السريري</strong>.',
    'home.cta':'ابدأ الآن',
    'home.how.title':'كيف يعمل','home.how.sub':'عملية فحص طبي دقيقة مصممة للوضوح والسلامة.',
    'home.how.video':'شاهد الشرح',
    'home.how.s1':'ارفع صورة الأشعة السينية بصيغة JPG أو PNG بشكل آمن.',
    'home.how.s2':'ينتظر نموذج الذكاء الاصطناعي لدينا معالجة الأنماط والشذوذات.',
    'home.how.s3':'استلم تقريرك الأولي.',
    'home.how.s4':'استشر أخصائياً طبياً لمراجعة نتائج الذكاء الاصطناعي.',
    'home.how.btn':'ابدأ التحليل التشخيصي الآن',
    'home.feat.title':'ما نقدمه','home.feat.sub':'من الفحص بالذكاء الاصطناعي إلى استشارة الخبراء.',
    'home.feat.ai.h':'تحليل الأشعة بالذكاء الاصطناعي','home.feat.ai.p':'ارفع صورة الأشعة واستلم تقييم المخاطر في ثوانٍ.',
    'home.feat.qa.h':'فضاء الأسئلة والأجوبة','home.feat.qa.p':'اسأل متخصصين طبيين معتمدين وتصفح قاعدة المعرفة.',
    'home.feat.log.h':'سجل الرحلة التشخيصية','home.feat.log.p':'تتبع كل فحص في جدول زمني مرئي.',
    'auth.login.h':'مرحباً بعودتك','auth.login.sub':'سجّل دخولك للوصول إلى حسابك',
    'auth.login.btn':'تسجيل الدخول','auth.login.forgot':'نسيت كلمة المرور؟','auth.login.new':'جديد هنا؟',
    'auth.login.create':'إنشاء حساب',
    'auth.reg.h':'أنشئ حسابك','auth.reg.sub':'انضم إلينا اليوم',
    'auth.reg.btn':'إنشاء حساب','auth.reg.already':'لديك حساب بالفعل؟','auth.reg.login':'تسجيل الدخول',
    'dash.welcome':'مرحباً،','dash.sub':'تتبع تقدمك الصحي واستشاراتك مع الخبراء.',
    'dash.scans':'الفحوصات التشخيصية','dash.consult':'الاستشارات الطبية','dash.answered':'المُجابة',
    'dash.history':'سجل الاستشارات','dash.date':'التاريخ','dash.question':'السؤال',
    'dash.status':'الحالة','dash.action':'الإجراء','dash.empty':'لم تطرح أسئلة بعد.',
    'dash.view':'عرض الإجابة','dash.waiting':'قيد الانتظار',
    'status.answered':'مُجاب','status.pending':'قيد الانتظار',
    'footer.connect':'تواصل معنا','footer.support':'الدعم السريري',
    'footer.copy':'© 2026 كانيا للأنظمة العصبية · واجهة التشخيص الداخلية',
    'scan.title':'الكشف عن مخاطر سرطان الرئة','scan.sub':'تحليل الأشعة السينية بالذكاء الاصطناعي',
    'scan.drop':'انقر أو اسحب صورة الأشعة السينية','scan.hint':'JPG وPNG مدعومان',
    'scan.btn':'تنفيذ فحص الكشف عن المخاطر','scan.loading':'جارٍ تحليل الشبكات العصبية…',
    'scan.high.title':'تنبيه: تم اكتشاف أنماط عالية الخطورة','scan.low.title':'سليم: أنماط منخفضة الخطورة',
    'notif.title':'الإشعارات','notif.sub':'ابقَ على اطلاع بنشاطك في كانيا',
    'notif.empty':'لا توجد إشعارات بعد','notif.all':'أنت على اطلاع بكل شيء!',
    'journey.title':'رحلتي التشخيصية','journey.sub':'سجل كامل بفحوصاتك',
    'journey.empty':'لا توجد فحوصات بعد','journey.start':'ابدأ أول فحص',
  }
};
function applyLang(lang) {
  const t = TRANSLATIONS[lang] || TRANSLATIONS.en;
  document.querySelectorAll('[data-i18n]').forEach(el => {
    const key = el.getAttribute('data-i18n');
    if (t[key] !== undefined) {
      if (el.getAttribute('data-i18n-html') === 'true') {
        el.innerHTML = t[key];
      } else {
        el.textContent = t[key];
      }
    }
  });
  document.documentElement.setAttribute('dir', lang === 'ar' ? 'rtl' : 'ltr');
  document.documentElement.setAttribute('lang', lang);
  document.querySelectorAll('.lang-btn').forEach(btn => {
    btn.classList.toggle('active', btn.getAttribute('data-lang') === lang);
  });
  localStorage.setItem('cania-lang', lang);
}
function applyTheme(theme) {
  document.documentElement.setAttribute('data-theme', theme);
  const icon = document.getElementById('themeIcon');
  if (icon) icon.className = theme === 'dark' ? 'bi bi-sun-fill' : 'bi bi-moon-fill';
  localStorage.setItem('cania-theme', theme);
}
function toggleTheme() {
  const current = document.documentElement.getAttribute('data-theme') || 'light';
  applyTheme(current === 'dark' ? 'light' : 'dark');
}
document.addEventListener('DOMContentLoaded', () => {
  const savedLang  = localStorage.getItem('cania-lang')  || 'en';
  const savedTheme = localStorage.getItem('cania-theme') || 'light';
  applyTheme(savedTheme);
  applyLang(savedLang);
  document.querySelectorAll('.lang-btn').forEach(btn => {
    btn.addEventListener('click', () => applyLang(btn.getAttribute('data-lang')));
  });
  const themeBtn = document.getElementById('themeToggleBtn');
  if (themeBtn) themeBtn.addEventListener('click', toggleTheme);
});
