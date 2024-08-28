import os

class Config:
    SQLALCHEMY_DATABASE_URI = 'postgresql://admin:tesT!01@localhost:5432/simpledb'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MAIL_SERVER = 'smtp.office365.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('cesar.garcia@ipsumtechnology.mx')
    MAIL_PASSWORD = os.environ.get('Faf73219')