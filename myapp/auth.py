from flask import Blueprint, render_template, redirect, url_for, flash, request
from . import db
from .models import User
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from .emails import send_confirmation_email

auth = Blueprint('auth', __name__)

@auth.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        user = User.query.filter_by(email=email).first()
        
        if user:
            flash('Email address already exists')
            return redirect(url_for('auth.register'))

        new_user = User(
            email=email,
            nombre=request.form.get('nombre'),
            apellido=request.form.get('apellido'),
            comida_favorita=request.form.get('comida_favorita'),
            artista_favorito=request.form.get('artista_favorito'),
            lugar_favorito=request.form.get('lugar_favorito'),
            color_favorito=request.form.get('color_favorito')
        )
        new_user.set_password(password)
        db.session.add(new_user)
        db.session.commit()

        send_confirmation_email(new_user)

        flash('A confirmation email has been sent to your email address.')
        return redirect(url_for('auth.login'))

    return render_template('register.html')

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        user = User.query.filter_by(email=email).first()
        
        if not user or not user.check_password(password):
            flash('Invalid email or password')
            return redirect(url_for('auth.login'))

        login_user(user)
        return redirect(url_for('main.dashboard'))

    return render_template('login.html')

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.home'))