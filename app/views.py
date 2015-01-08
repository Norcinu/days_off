from flask import render_template, flash, redirect
from app import app
from forms import LoginForm
from app import mongo
from app import db
import calendar
from werkzeug.exceptions import HTTPException
from models import User
from app import db
import requests

import calendar

@app.route('/')
@app.route('/index')
def index():
    usss = User.query.all()
    print usss
    try:
        cursor = mongo.db.days_off.find_one_or_404({'total_days_off':{'$gt':0}})
    except HTTPException as notfound:
        cursor = notfound
        return notfound.get_body() # perhaps dont want this to be quite so brutal.
    return render_template("index.html", title = 'Home', user = cursor)


@app.route('/login', methods = ['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Name='+form.name.data + ', remember_me='+str(form.remember_me.data))
        return redirect('/index')
    return render_template('login.html', title='Login', form=form)

@app.route('/update', methods = ['GET', 'POST'])
def update():
    calendar.setfirstweekday(calendar.SUNDAY)
    c = calendar.HTMLCalendar(calendar.SUNDAY).formatyear(2014)
    return c
    #return render_template('update.html', title='Update Date')


@app.route('/gaming')
def gaming():
    r = requests.get('http://eu.battle.net/api/d3/profile/norcinu-2227/')
    print r.json
    return render_template("gaming.html", title='Gaming', result=r.json)
