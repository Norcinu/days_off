from flask import Flask
from flask.ext.pymongo import PyMongo

#from pymongo import MongoClient

app = Flask(__name__)
app.config.from_object('config')

mongo = PyMongo(app)

from app import views
