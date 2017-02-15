from flask_wtf import Form
from wtforms import StringField, BooleanField
from wtforms.validators import DataRequired

class LoginForm(Form):
    userId = StringField('Login', validators=[DataRequired()])
    passId = StringField('Password', validators=[DataRequired()])
    remember_me = BooleanField('remember_me', default=False)