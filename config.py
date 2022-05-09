
class Config:
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://venecia:12345@localhost/pitcherapp'
    SECRET_KEY = 'os.eviron'

class ProdConfig(Config):
    pass

class TestConfig(Config):
    pass

class DevConfig(Config):
    DEBUG = True

config_options ={
      'production':ProdConfig,
      'development':DevConfig,
      'test': TestConfig
}