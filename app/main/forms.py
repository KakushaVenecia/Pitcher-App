from flask_wtf import FlaskForm
from wtforms import SubmitField,  TextAreaField, StringField, SelectField
from wtforms.validators import DataRequired



class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [DataRequired()])
    submit = SubmitField('Submit')

class NewPitchForm(FlaskForm):
    title = StringField ('Title', validators=[DataRequired()])
    post  = TextAreaField ('Best Shot', validators=[DataRequired()])
    category = SelectField ('Best Shot', choices=[('Inspiration','Inspiration'),('Freestyle','Freestyle'),('Famous Quotes', 'Famous Quotes')] ,validators=[DataRequired()])
    submit = SubmitField('Submit')

    