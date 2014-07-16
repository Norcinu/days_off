from flask import render_template, flash, redirect
from app import app
from forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
    user = [
                {
                    'author':{'nickname':'Steven'}, 
                    'id':'1'
                },
                {
                    'author':{'nickname':'Emilie'}, 
                    'id':'2'
                }
            ]
    return render_template("index.html", title = 'Home', user = user)


@app.route('/login', methods = ['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Name='+form.name.data + ', remember_me='+str(form.remember_me.data))
        return redirect('/index')
    return render_template('login.html', title='Login', form=form)
