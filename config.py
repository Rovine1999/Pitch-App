import os

class Config:

    
    SECRET_KEY='rovi123'
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringaschool:rovine5999@localhost/pitch'
    UPLOADED_PHOTOS_DEST ='app/static/photos'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
#  email configurations
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME='rovinewanjala99@gmail.com'
    SQLALCHEMY_DATABASE_URI ='DATABASE_URL'
    MAIL_PASSWORD ='Rovine1999'
    SENDER_EMAIL = 'rovinewanjala99@gmail.com'
    SIMPLEMDE_JS_IIFE = True
    SIMPLEMDE_USE_CDN = True

class ProdConfig(Config):
   SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")




class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringaschool:Rovine1999@localhost/pitch'

class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringaschool:Rovine1999@localhost/pitch'
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig,
'test':TestConfig
}