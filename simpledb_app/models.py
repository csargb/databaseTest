from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
#from sqlalchemy.sql import func

db = SQLAlchemy()

class User(db.Model):
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


class Questions(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    favorite_food = db.Column(db.String(100), nullable=False)
    favorite_artist = db.Column(db.String(100), nullable=False)
    favorite_place = db.Column(db.String(100), nullable=False)
    favorite_color = db.Column(db.String(100), nullable=False)