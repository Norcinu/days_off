from flask.ext.wtf import Form
from wtforms import TextField, BooleanField
from wtforms.validators import Required

class LoginForm(Form):
    name = TextField('name', validators = [Required()])
    remember_me = BooleanField('remember_me', default=False)

