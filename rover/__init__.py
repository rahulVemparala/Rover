"""
Package file for our application : rover
initialize flask app and sqlalchemy DB
"""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager


app = Flask(__name__)
app.config['SECRET_KEY'] = "ea8af9fdf1f57149062f3985e62114b4"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app=app)
bcrypt = Bcrypt(app=app)
login_manager = LoginManager(app=app) 
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'
# this import should be after app and db initialization ,to avoid circular imports

from rover.routes import home, about, register, login