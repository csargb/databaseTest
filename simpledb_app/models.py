from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
#from sqlalchemy.sql import func


db = SQLAlchemy()


login_manager = LoginManager()
login_manager.login_view = '/login/'


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text, nullable=False)
    lastname = db.Column(db.Text, nullable=False)
    email = db.Column(db.Text, unique=True, nullable=False)
    password_hash = db.Column(db.Text, nullable=False)

    def __init__(self, name, lastname, email):
        self.name = name
        self.lastname = lastname
        self.email = email

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class Questions(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    favorite_food = db.Column(db.Text, nullable=False)
    favorite_artist = db.Column(db.Text, nullable=False)
    favorite_place = db.Column(db.Text, nullable=False)
    favorite_color = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __init__(self, favorite_food, favorite_artist, favorite_place, favorite_color, user_id):
        self.favorite_food = favorite_food
        self.favorite_artist = favorite_artist
        self.favorite_place = favorite_place
        self.favorite_color = favorite_color
        self.user_id = user_id