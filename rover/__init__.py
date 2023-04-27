"""
Package file for our application : rover
initialize flask app and sqlalchemy DB
"""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__)
app.config['SECRET_KEY'] = "ea8af9fdf1f57149062f3985e62114b4"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app=app)


# this import should be after app and db initialization ,to avoid circular imports

from rover.routes import *