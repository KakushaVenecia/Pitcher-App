import app
from . import main
from .forms import NewPitchForm, UpdateProfile
from flask_login import current_user, login_required
from ..models import Pitch, User
from flask import render_template,request,redirect,url_for,abort
from .. import db, photos


@main.route('/')
def index():
    pitches = Pitch.query.all()
    return render_template('home.html', pitches = pitches )

@main.route('/about')
def about():
    return render_template('about.html')

@main.route('/pitches/<string:id>')
def pitches(id):
    return render_template('pitches.html', id =id )

@main.route('/pitchs')
def pitchs(id):
    return render_template ('pitchs.html', id=id)

@main.route('/newpitch', methods = ['GET','POST'])  
def newPitch():
    form = NewPitchForm() 
    if form.validate_on_submit():
        title = form.title.data
        post = form.post.data
        category = form.category.data
        user_id = current_user
        new_pitch = Pitch( title =title, post = post, category = category)
        new_pitch.save_pitch()
        return redirect (url_for('main.index'))
    return render_template ('newpitch.html', form = form)
# @main.route('/login', methods=['GET','POST'])
# def login():
#     login = LoginForm()
#     return render_template ('login.html', login = login )

# @main.route('/signin', methods=['GET','POST'])
# def signin():
#     form = RegisterForm()
#     return render_template('signin.html', form = form)

@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))

    return render_template('profile/update.html',form =form)

@main.route('/user/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))