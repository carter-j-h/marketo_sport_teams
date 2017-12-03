from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import LoginManager
from flask.ext.mail import Mail

app = Flask(__name__)
# reads all data from config.py file and uses it in the app
app.config.from_object('config')
db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)

# Flask-Mail configuration
mail = Mail(app)

from app import views, models
