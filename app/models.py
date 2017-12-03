from app import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask.ext.login import UserMixin
from datetime import datetime

summary = db.Table('summary',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
    db.Column('team_id', db.Integer, db.ForeignKey('team.id'))
)


class User(UserMixin, db.Model):
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(64), index=True, unique=True)
	email = db.Column(db.String(120), index=True, unique=True)
	password_hash = db.Column(db.String(128))
	teams = db.relationship('Team', secondary= summary, backref=db.backref('users', lazy='dynamic'), lazy='dynamic')


	# way to instance a class and assign all relevant variables
	def __init__(self, username, email, password):
		self.username = username
		self.email = email
		self.set_password(password)
		

	# @property
	# def password(self):
	# 	raise AttributeError('password is not a readable attribute')

	# @password.setter
	def set_password(self, password):
		self.password_hash = generate_password_hash(password)
	def verify_password(self, password):
		return check_password_hash(self.password_hash, password)


	
	def __repr__(self):
		return'<User %r>' % self.username

class Team(db.Model):
	
	id = db.Column(db.Integer, primary_key=True)
	team = db.Column(db.String(140))
	league = db.Column(db.String(140))
	
	
	def __init__(self, team, league):
		self.team = team
		self.league = league 

	def __repr__(self):
		return '<Team %r>' % self.team






