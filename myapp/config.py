import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'your_secret_key'
    SQLALCHEMY_DATABASE_URI = 'postgresql://databasetest_guv7_user:zjrvahyjGtNb4uuyqdpN577WkReUD9H8@dpg-cr6ubmi3esus7393hhlg-a.oregon-postgres.render.com/databasetest_guv7'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MAIL_SERVER = 'smtp.office365.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('cesar.garcia@ipsumtechnology.mx')
    MAIL_PASSWORD = os.environ.get('Faf73219')