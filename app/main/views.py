from atexit import register
import app
from . import main
from flask import render_template
from ..data import Pitch
from .forms import LoginForm , RegisterForm


Pitches = Pitch()


@main.route('/')
def index():
    return render_template('home.html')

# @main.route('/about')
# def about():
#     return render_template ('about.html')

@main.route('/pitches/<string:id>')
def pitches(id):
    return render_template('pitches.html', id =id )


@main.route('/pitchs')
def pitchs(id):
    return render_template ('pitchs.html', id=id)

@main.route('/login', methods=['GET','POST'])
def login():
    login = LoginForm()
    return render_template ('login.html', login = login )

@main.route('/signin', methods=['GET','POST'])
def signin():
    # register = RegisterForm
    form = RegisterForm()
    return render_template('signin.html', form = form)
