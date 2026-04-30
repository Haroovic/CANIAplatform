from flask import render_template,url_for,flash,redirect,request
from extensions import db,login_manager
from flask_bcrypt import Bcrypt
from flask import Flask
from flask_login import login_user,current_user,logout_user,login_required
from flask_migrate import Migrate
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'
bcrypt = Bcrypt()
app = Flask(__name__)
app.config['SECRET_KEY']='a6dbe89df46cd9b4e7331d2ebcc54e6afdd7427d5ee5592ef506c451e0aa5c13'
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///cania.db'
db.init_app(app)
login_manager.init_app(app)
from models import User, Document
from forms import RegistrationForm,LoginForm
migrate=Migrate(app,db)
names=[{'first_name':'mounib','last_name':'mohamed'},
       {'first_name':'bonheur','last_name':'amine'}]
helps=[{'name':'mounib','icon':'mohamed','description':'this is help'}
       ]
@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html',helps=helps)
@app.route("/about")
def about():
    return render_template('about.html',names=names,title="about")
@app.route("/register",methods=['GET','POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(fname=form.fname.data,lname=form.lname.data,username = form.username.data, email=form.email.data , password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash(f"the account been created succesfully for {form.username.data}",'success')
        return redirect(url_for('login'))
    return render_template('register.html',names=names,title="Register",form=form)
@app.route("/login",methods=['GET','POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if (user and bcrypt.check_password_hash(user.password,form.password.data)):
            login_user(user,remember=form.remember.data)
            next_page =request.args.get('next')
            flash(f"login succesful",'success')
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            flash(f"Login unseeccessful please check credentials",'danger')
    return render_template('login.html',names=names,title="Login",form=form)
@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))
@app.route("/dashboard")
@login_required
def dashboard():
    return render_template('dashboard.html',title="Dashborad")
if __name__=="__main__":
    app.run(debug=True,port=5001)
