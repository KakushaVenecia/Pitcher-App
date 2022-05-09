from flask import Flask
from flask_bootstrap import Bootstrap
from config import config_options
from flask_sqlalchemy import SQLAlchemy


# app.config['SECRET_KEY']= "this is good"

# registration = RegisterForm ()
# Login = LoginForm()

bootstrap = Bootstrap()

db = SQLAlchemy()

def create_app(config_name):
    app = Flask(__name__)

# Creating the app configurations
    app.config.from_object(config_options[config_name])

    # Initializing flask extensions
    bootstrap.init_app(app)

    #Initializing data base 
    db.init_app(app)

    # Registering the blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app



