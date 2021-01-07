import os

class Config(object):
    SECRET_KEY = 'qeqweqweqwewq'
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USER_SSL = False
    MAIL_USER_TLS = True
    MAIL_USERNAME = "prueba@prueba.com"
    MAIL_PASSWORD = os.environ.get('PASSWORD_EMAIL_CF')

class DevelopmentConfig(Config):
    DEBUG=True
    SQLALCHEMY_DATABASE_URI = 'mysql://root:@localhost/flask'
    SQLALCHEMY_TRACK_MODIFICATIONS = False