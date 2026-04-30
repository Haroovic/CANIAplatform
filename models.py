from datetime import datetime
from extensions import db
from flask_login import UserMixin
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    fname = db.Column(db.String(25), nullable=False)
    lname = db.Column(db.String(25), nullable=False)
    username = db.Column(db.String(25), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    role = db.Column(db.String(20), nullable=True, default="patient")
    documents = db.relationship('Document', backref='author', lazy=True)
    questions = db.relationship('Question', backref='asker', lazy=True, foreign_keys='Question.user_id')
    notifications = db.relationship('Notification', backref='recipient', lazy=True)
    def __repr__(self):
        return f"User('{self.fname}','{self.lname}','{self.username}','{self.role}','{self.email}')" 
class Document(db.Model):
    id = db.Column(db.String(36), primary_key=True)
    file_path = db.Column(db.String(200), nullable=False)
    prediction = db.Column(db.String(200))
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    def __repr__(self):
        return f"Document('{self.file_path}', '{self.id}', '{self.prediction}', {self.user_id})"
class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question_text = db.Column(db.Text, nullable=False)
    keywords = db.Column(db.String(200))  # Comma-separated keywords
    answer_text = db.Column(db.Text)  # Can be null if unanswered
    is_answered = db.Column(db.Boolean, default=False)
    is_expert_created = db.Column(db.Boolean, default=False)  # True if expert created it
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    date_answered = db.Column(db.DateTime)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))  # The patient/user asking
    answered_by = db.Column(db.Integer, db.ForeignKey('user.id'))  # The expert answering
    def __repr__(self):
        return f"Question('{self.question_text[:30]}...', answered={self.is_answered})"
class Notification(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    message = db.Column(db.String(300), nullable=False)
    is_read = db.Column(db.Boolean, default=False)
    link = db.Column(db.String(200))  # Link to the relevant page
    date_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    def __repr__(self):
        return f"Notification('{self.message[:20]}...', read={self.is_read})"
