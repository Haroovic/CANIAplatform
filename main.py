import os
import uuid
import pandas as pd
import torch
import torch.nn as nn
import torch.nn.functional as F
import torchxrayvision as xrv
from PIL import Image
import numpy as np
import io
from datetime import datetime
from dotenv import load_dotenv
load_dotenv()
from flask import render_template, url_for, flash, redirect, request, Flask, jsonify
from extensions import db, login_manager
from flask_bcrypt import Bcrypt
from flask_login import login_user, current_user, logout_user, login_required
from flask_migrate import Migrate
class MedicalClassifier(nn.Module):
    def __init__(self, base_model):
        super(MedicalClassifier, self).__init__()
        self.features = base_model.features
        num_features = base_model.classifier.in_features
        self.classifier = nn.Sequential(
            nn.Linear(num_features, 256),
            nn.BatchNorm1d(256),
            nn.ReLU(),
            nn.Dropout(0.4),
            nn.Linear(256, 2)
        )
    def forward(self, x):
        features = self.features(x)
        out = F.relu(features, inplace=True)
        out = F.adaptive_avg_pool2d(out, (1, 1))
        out = torch.flatten(out, 1)
        return self.classifier(out)
DEVICE = torch.device("cpu")
base_densenet = xrv.models.DenseNet(weights="densenet121-res224-all")
ai_model = MedicalClassifier(base_densenet)
MODEL_PATH = os.path.join(os.getcwd(), 'medical_stage2_auc_best.pth')
if os.path.exists(MODEL_PATH):
    ai_model.load_state_dict(torch.load(MODEL_PATH, map_location=DEVICE))
    ai_model.eval()
    print("[OK] Medical Model Loaded Successfully")
else:
    print(f"[WARNING] Model file not found at {MODEL_PATH}")
app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'fallback-dev-key-change-in-production')
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('SQLALCHEMY_DATABASE_URI', 'sqlite:///cania.db')
app.config['UPLOAD_FOLDER'] = os.path.join('static', 'uploads')
db.init_app(app)
bcrypt = Bcrypt(app)
login_manager.init_app(app)
migrate = Migrate(app, db)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'
from models import User, Document, Question, Notification
from forms import RegistrationForm, LoginForm, QuestionForm, ExpertQuestionForm
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
def find_matching_questions(search_query):
    if not search_query:
        return []
    search_query = search_query.lower().strip()
    search_words = set(search_query.split())
    all_questions = Question.query.filter_by(is_answered=True).all()
    scored_questions = []
    for q in all_questions:
        if not q.keywords:
            continue
        keywords = [k.strip().lower() for k in q.keywords.split(',')]
        matches = sum(1 for word in search_words if any(word in keyword or keyword in word for keyword in keywords))
        if matches > 0:
            scored_questions.append((q, matches))
    scored_questions.sort(key=lambda x: x[1], reverse=True)
    return [q[0] for q in scored_questions[:5]]
@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')
@app.route("/about")
def about():
    return render_template('about.html', title="About CANIA")
@app.route("/help")
def help_page():
    return render_template('help.html', title="Help Center")
@app.route("/scanner")
@login_required
def scanner():
    if current_user.role != "patient":
        flash("Only patients can access the scanner.", "warning")
        return redirect(url_for('home'))
    return render_template("scanner.html")
@app.route("/upload", methods=["POST"])
@login_required
def upload():
    if current_user.role != "patient":
        return jsonify({"status": "error", "message": "Only patients can upload scans"}), 403
    if 'file' not in request.files:
        return jsonify({"status": "error", "message": "No file selected"}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({"status": "error", "message": "No file selected"}), 400
    if not os.path.exists(app.config['UPLOAD_FOLDER']):
        os.makedirs(app.config['UPLOAD_FOLDER'])
    ext = os.path.splitext(file.filename)[1]
    unique_filename = str(uuid.uuid4()) + ext
    save_path = os.path.join(app.config['UPLOAD_FOLDER'], unique_filename)
    file.save(save_path)
    try:
        img = Image.open(save_path).convert('L').resize((320, 320))
        img_np = (np.array(img) / 255.0) * 2048.0 - 1024.0
        tensor = torch.from_numpy(img_np).float().unsqueeze(0).unsqueeze(0)
        with torch.no_grad():
            output = ai_model(tensor)
            prob = F.softmax(output, dim=1)
            _, predicted = torch.max(prob, 1)
            prediction_val = predicted.item() 
        doc = Document(id=str(uuid.uuid4()), file_path=unique_filename, prediction=str(prediction_val), user_id=current_user.id)
        db.session.add(doc)
        db.session.commit()
        return jsonify({"status": "success", "prediction": str(prediction_val)})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500
@app.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(fname=form.fname.data, lname=form.lname.data, username=form.username.data, 
                    email=form.email.data, role=form.role.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash(f"Account created successfully for {form.username.data}", 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title="Register", form=form)
@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            flash("Login successful", 'success')
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            flash("Login unsuccessful, please check credentials", 'danger')
    return render_template('login.html', title="Login", form=form)
@app.route("/logout")
def logout():
    logout_user()
    flash("You have been logged out.", "info")
    return redirect(url_for('home'))
@app.route("/dashboard")
@login_required
def dashboard():
    user_questions = Question.query.filter_by(user_id=current_user.id).order_by(Question.date_posted.desc()).all()
    scan_count = Document.query.filter_by(user_id=current_user.id).count()
    return render_template('dashboard.html', title="Dashboard", questions=user_questions, scan_count=scan_count)
@app.route("/cania-space", methods=['GET', 'POST'])
@login_required
def cania_space():
    if current_user.role != "patient":
        flash("Only patients can access CANIA Space.", "warning")
        return redirect(url_for('home'))
    form = QuestionForm()
    search_query = request.args.get('search', '')
    matched_questions = []
    if search_query:
        matched_questions = find_matching_questions(search_query)
    if form.validate_on_submit():
        new_question = Question(question_text=form.question_text.data, user_id=current_user.id, is_expert_created=False)
        db.session.add(new_question)
        db.session.commit()
        experts = User.query.filter_by(role='expert').all()
        for expert in experts:
            notification = Notification(
                user_id=expert.id, 
                message=f"New question from {current_user.username}: {form.question_text.data[:50]}...", 
                link=url_for('answer_question', question_id=new_question.id)
            )
            db.session.add(notification)
        db.session.commit()
        flash("Your question has been submitted! Experts will be notified.", "success")
        return redirect(url_for('cania_space'))
    unread_count = Notification.query.filter_by(user_id=current_user.id, is_read=False).count()
    return render_template('cania_space.html', title="CANIA Space", form=form, search_query=search_query, matched_questions=matched_questions, unread_count=unread_count)
@app.route("/cania-space/question/<int:question_id>")
@login_required
def view_question(question_id):
    question = Question.query.get_or_404(question_id)
    return render_template('view_question.html', question=question)
@app.route("/expert-dashboard", methods=['GET', 'POST'])
@login_required
def expert_dashboard():
    if current_user.role != "expert":
        flash("Only experts can access the expert dashboard.", "warning")
        return redirect(url_for('home'))
    form = ExpertQuestionForm()
    if form.validate_on_submit():
        new_qa = Question(
            question_text=form.question_text.data, 
            keywords=form.keywords.data, 
            answer_text=form.answer_text.data, 
            is_answered=True, 
            is_expert_created=True, 
            answered_by=current_user.id, 
            date_answered=datetime.utcnow()
        )
        db.session.add(new_qa)
        db.session.commit()
        flash("Q&A added successfully!", "success")
        return redirect(url_for('expert_dashboard'))
    unanswered_questions = Question.query.filter_by(is_answered=False, is_expert_created=False).order_by(Question.date_posted.desc()).all()
    all_qas = Question.query.filter_by(is_answered=True).order_by(Question.date_posted.desc()).all()
    unread_count = Notification.query.filter_by(user_id=current_user.id, is_read=False).count()
    return render_template('expert_dashboard.html', title="Expert Dashboard", form=form, unanswered_questions=unanswered_questions, all_qas=all_qas, unread_count=unread_count)
@app.route("/expert/answer/<int:question_id>", methods=['GET', 'POST'])
@login_required
def answer_question(question_id):
    if current_user.role != "expert":
        flash("Only experts can answer questions.", "warning")
        return redirect(url_for('home'))
    question = Question.query.get_or_404(question_id)
    form = ExpertQuestionForm()
    if request.method == 'GET':
        form.question_text.data = question.question_text
    if form.validate_on_submit():
        question.answer_text = form.answer_text.data
        question.keywords = form.keywords.data
        question.is_answered = True
        question.answered_by = current_user.id
        question.date_answered = datetime.utcnow()
        if question.user_id:
            notification = Notification(
                user_id=question.user_id, 
                message=f"Expert {current_user.fname} has answered your question!", 
                link=url_for('view_question', question_id=question.id)
            )
            db.session.add(notification)
        db.session.commit()
        flash("Answer submitted successfully and question is now searchable!", "success")
        return redirect(url_for('expert_dashboard'))
    return render_template('answer_question.html', question=question, form=form)
@app.route("/notifications")
@login_required
def notifications():
    user_notifications = Notification.query.filter_by(user_id=current_user.id).order_by(Notification.date_created.desc()).all()
    response = render_template('notifications.html', notifications=user_notifications)
    for notif in user_notifications:
        notif.is_read = True
    db.session.commit()
    return response
@app.route("/my-journey")
@login_required
def my_journey():
    if current_user.role != "patient":
        flash("Only patients can access their journey.", "warning")
        return redirect(url_for('home'))
    documents = Document.query.filter_by(user_id=current_user.id).order_by(Document.date_posted.desc()).all()
    return render_template('journey.html', title="My Journey", documents=documents)
if __name__ == "__main__":
    app.run(debug=True, port=5001)
