from flask import Flask
#from flask.ext.pymongo import PyMongo

from pymongo import MongoClient

app = Flask(__name__)
app.config.from_object('config')

mongo = MongoClient('mongodb://days:skunkpussy@ds029817.mongolab.com:29817/steve_srwc')

#PyMongo(app, config_prefix='MONGO')

from app import views
