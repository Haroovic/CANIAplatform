from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField, SelectField
from wtforms.validators import DataRequired, Length, Regexp, EqualTo, ValidationError
from models import User
class RegistrationForm(FlaskForm):
    fname = StringField('First Name', validators=[DataRequired(), Length(min=2, max=20)])
    lname = StringField('Last Name', validators=[DataRequired(), Length(min=2, max=20)])
    username = StringField(
        "Username", validators=[DataRequired(), Length(min=2, max=25)]
    )
    email = StringField('Email', validators=[
        DataRequired(), 
        Regexp(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', message="Invalid email address")
    ])
    password = PasswordField('Password', validators=[
        DataRequired(), 
        Regexp(
            regex=r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$',
            message="Password must be at least 8 characters, include uppercase, lowercase, number and special character"
        )
    ])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    role = SelectField(
        "Account Type",
        choices=[("patient", "Patient"), ("expert", "Medical Expert")],
        validators=[DataRequired()]
    )
    submit = SubmitField('Sign Up')
    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('Username already exists. Please choose another one.')
    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('Email already exists. Please choose another one.')
class LoginForm(FlaskForm):
    email = StringField('Email', validators=[
        DataRequired(), 
        Regexp(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', message="Invalid email address")
    ])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')
class QuestionForm(FlaskForm):
    question_text = TextAreaField('Ask your question...', validators=[DataRequired(), Length(min=10, max=500)])
    submit = SubmitField('Submit Question')
class ExpertQuestionForm(FlaskForm):
    question_text = TextAreaField('Question', validators=[DataRequired(), Length(min=10, max=500)])
    keywords = StringField('Keywords (comma-separated)', validators=[DataRequired(), Length(max=200)])
    answer_text = TextAreaField('Answer', validators=[DataRequired(), Length(min=10, max=2000)])
    submit = SubmitField('Add to Knowledge Base')
