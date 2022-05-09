from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class RegisterForm(FlaskForm):
    username= StringField ("What your User Name", validators=[DataRequired()])
    emailaddress =StringField ("What your Email Name", validators=[DataRequired()])
    password = StringField ("What your Password", validators=[DataRequired()])
    confirm_password = StringField ("Confirm Password", validators=[DataRequired()])
    submit = SubmitField("Submit")

class LoginForm(FlaskForm):
    username= StringField ("What your User Name", validators=[DataRequired()])
    password = StringField ("What your Password", validators=[DataRequired()])
    submit = SubmitField("Submit")
