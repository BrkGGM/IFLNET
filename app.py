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


class RegisterForm(FlaskForm):
    username = StringField(validators=[
                           InputRequired(), Length(min=4, max=20)], render_kw={"placeholder": "Kullanıcı Adı"})

    password = PasswordField(validators=[
                             InputRequired(), Length(min=8, max=20)], render_kw={"placeholder": "Şifre"})
    
    kod = StringField(validators=[
                             InputRequired(), Length(min=8, max=20)], render_kw={"placeholder": "Kayıt Kodu"})
    
    submit = SubmitField('Kayıt Ol')

    def validate_username(self, username):

        username_value = username.data

        regex = r"^[A-Za-z0-9_.]+$"
        if not re.match(regex, username_value):
            flash("Kullanıcı adı yalnızca harf, sayı, alt çizgi ve nokta içermelidir.")
            raise ValidationError("Kullanıcı adı yalnızca harf, sayı, alt çizgi ve nokta içermelidir.")

        existing_user_username = User.query.filter_by(
            username=username.data.lower()).first()
        if existing_user_username:
            flash('Bu kullanıcı adı zaten mevcut, lütfen başka bir kullanıcı adı seçiniz.')
            raise ValidationError('Bu kullanıcı adı zaten mevcut, lütfen başka bir ad seçiniz.')


class LoginForm(FlaskForm):
    username = StringField(validators=[
                           InputRequired(), Length(min=4, max=20)], render_kw={"placeholder": "Kullanıcı Adı"})

    password = PasswordField(validators=[
                             InputRequired(), Length(min=8, max=20)], render_kw={"placeholder": "Şifre"})

    submit = SubmitField('Giriş Yap')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if not user:
            
            flash("Kullanıcı adı veya şifre hatalı.")
            raise ValidationError("Kullanıcı adı veya şifre hatalı.")
            return(user)
        
@app.before_request
def make_session_permanent():
    session.permanent = True 

@app.route('/')
def home():
    if current_user.is_authenticated:
        return  "Merhaba Dünya"
    else:
        return "Lütfen giriş yapın"




@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data.lower()).first()
        if user:
            if bcrypt.check_password_hash(user.password, form.password.data):
                login_user(user)
                #user.last_login_device = request.user_agent.string
                #user.last_login_ip = request.remote_addr
                db.session.commit()

                return redirect(url_for('home'))
            else:
                flash("Kullanıcı adı veya şifre hatalı.")
                
    return render_template('login.html', form=form)


@ app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()

    if form.validate_on_submit():
        if form.kod.data == 'iflhub2024':

            hashed_password = bcrypt.generate_password_hash(form.password.data)
            new_user = User(username=form.username.data.lower(), password=hashed_password)
            db.session.add(new_user)
            db.session.commit()
            return redirect(url_for('login'))
        else:
            flash("Kayıt kodu yanlış!")
            return redirect(url_for('register'))

    return render_template('register.html', form=form)


if __name__ == "__main__":
    #from waitress import serve
    #serve(app, host="87.248.157.245", port=8080)
    app.run(debug=True)
