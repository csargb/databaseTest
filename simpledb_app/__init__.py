import os

from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, login_required
#from  config import Config

db = SQLAlchemy()
login_manager = LoginManager()

def create_app():
    app = Flask(__name__)
    #app.config.from_object(Config)
    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'

    #from .routes import main
    #from .auth import auth

    #app.register_blueprint(main)
    #app.register_blueprint(auth, url_prefix='/auth')

    #main = Blueprint('main', __name__)

    @app.route('/')
    def home():
        return render_template('home.html')

    #@login_required
    #@app.route('/dashboard/')
    #def dashboard():
        #return render_template('dashboard.html')

    @app.route('/login/')
    def login():
        return render_template('login.html')

    return app