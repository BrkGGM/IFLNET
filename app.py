from flask import Flask, render_template, url_for, redirect, request, flash, session
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, logout_user, current_user
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length, ValidationError, DataRequired
from flask_bcrypt import Bcrypt
from datetime import datetime, timezone
from datetime import timedelta
from flask_migrate import Migrate
import re


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SECRET_KEY'] = 'SANSÜR' #Burayı sen değiştirip saklayacaksın önemli!
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
migrate = Migrate(app, db)


login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'


ADMIN_USERNAMES = {'admin','yozgat.m66','bay.beyaz'}  


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
                          

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=True, nullable=True) 
    username = db.Column(db.String(20), nullable=False, unique=True)
    password = db.Column(db.String(80), nullable=False)

class Yazilar(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    message = db.Column(db.String(10000), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    baslik = db.Column(db.String(50), nullable=False, unique=True)






@app.before_request
def make_session_permanent():
    session.permanent = True 

@app.route('/')
def home():
    if current_user.is_authenticated:
        yazilar = Yazilar.query.all()
        return  render_template('home.html', yazilar = yazilar)
    else:
        return "Lütfen giriş yapın"



@app.route('/login', methods=['GET', 'POST'])
def login():
    
    if request.method == 'POST':
        password = request.form.get('password')
        username = request.form.get('username')
        user = User.query.filter_by(username=username.lower()).first()
        if user:
            if bcrypt.check_password_hash(user.password, password):
                login_user(user)
                #user.last_login_device = request.user_agent.string
                #user.last_login_ip = request.remote_addr
                db.session.commit()

                return redirect(url_for('home'))
            else:
                flash("Kullanıcı adı veya şifre hatalı.")
                
    return render_template('login.html')


@ app.route('/register', methods=['GET', 'POST'])
def register():
    

    if request.method == 'POST':
        password = request.form.get('password')
        username = request.form.get('username')
        email = request.form.get('email')

        hashed_password = bcrypt.generate_password_hash(password)
        new_user = User(username=username.lower(), password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('login'))
        

    return render_template('register.html')



@app.route('/yaziyaz' , methods=['GET', 'POST'])
@login_required
def yazi_yaz():

    if request.method == 'POST':
        if current_user.is_authenticated:
            user_info = User.query.get(current_user.id)


            data = request.form.get('yazi')
            baslik = request.form.get('baslik')

            new_itiraf = Yazilar(message=data, user_id=current_user.id, baslik = baslik)   
            db.session.add(new_itiraf)
            db.session.commit()
            

    return render_template('yazi_yaz.html')

@app.route('/yazi/<yazi_baslik>')
def yazi(yazi_baslik):
    yazi = Yazilar.query.get(yazi_baslik)
    if yazi:
        return render_template('yazi.html', yazi =yazi)
    return redirect(url_for('home'))
if __name__ == "__main__":
    #from waitress import serve
    #serve(app, host="87.248.157.245", port=8080)
    app.run(debug=True)
