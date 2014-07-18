from flask import render_template, flash, redirect
from app import app
from forms import LoginForm
from app import mongo
import calendar
from werkzeug.exceptions import HTTPException

@app.route('/')
@app.route('/index')
def index():
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
    return render_template('update.html', title='Update Date')
