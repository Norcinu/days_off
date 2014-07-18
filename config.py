import os

CSRF_ENABLED = True
SECRET_KEY = os.getenv('FLASK_FORM_KEY')

MONGO_HOST = os.getenv('MONGO_MYHOST')
MONGO_PORT = os.getenv('MONGO_MYPORT')
MONGO_DBNAME = os.getenv('MONGO_DB')
MONGO_USERNAME = os.getenv('MONGO_UNAME')
MONGO_PASSWORD = os.getenv('MONGO_PWD')

