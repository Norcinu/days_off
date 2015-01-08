from flask import Flask
from flask.ext.pymongo import PyMongo
from flask.ext.sqlalchemy import SQLAlchemy

#from pymongo import MongoClient

app = Flask(__name__)
app.config.from_object('config')
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://pfrgwbtg_mrgleed:skunkpussy@91.103.216.2:3306/pfrgwbtg_flask'

db = SQLAlchemy(app)
mongo = PyMongo(app)


from app import views
