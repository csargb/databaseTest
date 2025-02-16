import os


from flask import Flask, render_template, url_for, redirect
from werkzeug.security import generate_password_hash, check_password_hash
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo
from flask_migrate import Migrate
from flask_login import login_user, login_required, logout_user, current_user
from models import db, login_manager, User, Questions


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:hTn51_nC!:@localhost:5432/simpledb'
app.config['SECRET_KEY'] = '0123456789'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db.init_app(app)
login_manager.init_app(app)


migrate = Migrate(app, db)


class RegistrationForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    lastname = StringField('Lastname', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')


class QuestionsForm(FlaskForm):
    favorite_food = StringField('Favorite food', validators=[DataRequired()])
    favorite_artist = StringField('Favorite artist', validators=[DataRequired()])
    favorite_place = StringField('Favorite place', validators=[DataRequired()])
    favorite_color = StringField('Favorite color', validators=[DataRequired()])
    submit = SubmitField('Save answers')


@app.route('/')
def index():
    return render_template('home.html')


@app.route('/login/', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data

        # Retrieve the user from the database
        user = User.query.filter_by(email=email).first()

        if user and user.check_password(password):
            login_user(user)
            return redirect(url_for('questions'))
        else:
            return 'Invalid username or password.'
        
    return render_template('login.html', form=form)


@app.route('/register/', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        name = form.name.data
        lastname = form.lastname.data
        email = form.email.data
        password = form.password.data

        # Create a new user and set their password
        user = User(name=name, lastname=lastname, email=email)
        user.set_password(password)

        # Add the user to the database
        db.session.add(user)
        db.session.commit()

        return redirect(url_for('login'))
    
    else:
        print(form.errors)
    
    return render_template('register.html', form=form)


@app.route('/questions/', methods=['GET', 'POST'])
@login_required
def questions():
    form = QuestionsForm()
    if form.validate_on_submit():
        favorite_food = form.favorite_food.data
        favorite_artist = form.favorite_artist.data
        favorite_place = form.favorite_place.data
        favorite_color = form.favorite_color.data
        user_id = current_user.id

        #Create record
        questions = Questions(favorite_food=favorite_food, favorite_artist=favorite_artist, favorite_place=favorite_place, favorite_color=favorite_color)

        db.session.add(questions)
        db.session.commit()

        return redirect(url_for('display'))

    return render_template('questions.html', form=form)


@app.route('/logout/', methods=['GET', 'POST'])
@login_required
def logout():
    logout_user()

    return redirect(url_for('login'))


@app.route('/records/', methods=['GET', 'POST'])
@login_required
def display():
    Questions.query.add_column(favorite_food='Pizza')

    return render_template('records.html')