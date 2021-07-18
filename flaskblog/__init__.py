from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import form
from sqlalchemy.orm import backref

app = Flask(__name__)
app.config['SECRET_KEY'] = '24ee0c10cc86e98d7eb9fcc08611d46b'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
db = SQLAlchemy(app)

from flaskblog import routes
