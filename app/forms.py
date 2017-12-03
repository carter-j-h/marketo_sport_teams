from flask.ext.wtf import Form
from wtforms import StringField, TextField, PasswordField, validators
from wtforms.validators import DataRequired, EqualTo
from models import User

class LoginForm(Form):
	username = TextField('Username', validators=[DataRequired(), validators.Length(min=3, max=15)])
	email = TextField('Email Address', validators= [DataRequired(), validators.Length(min=6, max=25)])
	password = PasswordField('Password', validators= [DataRequired(), validators.Length(min=3, max=25)])



class RegistrationForm(Form):
	username = TextField('Pick a Username', validators=[DataRequired(), validators.Length(min=3, max=15)])
	email = TextField('Enter you Email Address', validators= [DataRequired(), validators.Length(min=6, max=25)])
	password = PasswordField('Enter a Password- Choose Wisely!', validators= [DataRequired(), EqualTo('password2', message='Passwords much match'), validators.Length(min=3, max=25)])
	password2 = PasswordField('Confirm password', validators=[DataRequired()])
	

def validate_email(self, field):
	if models.User.query.filter_by(email=field.data).first():
		raise ValidationError('Email already registered')

def validate_username(self, field):
	if models.User.query.filter_by(username=field.data).first():
		raise ValidationError('Username already in use')