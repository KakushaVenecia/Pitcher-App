import os


class Config:
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://venecia:12345@localhost/pitcherapp'
    SECRET_KEY =os.environ.get('SECRET_KEY')
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME= os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD= os.environ.get('MAIL_PASSWORD')
    UPLOADED_PHOTOS_DEST ='app/static/photos'


class ProdConfig(Config):
    # SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://venecia:12345@localhost/pitcherapp'
    pass

class TestConfig(Config):
    pass

class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://venecia:12345@localhost/pitcherapp'
    DEBUG = True

config_options ={
      'production':ProdConfig,
      'development':DevConfig,
      'test': TestConfig
}