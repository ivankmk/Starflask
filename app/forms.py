from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

# https://wtforms.readthedocs.io/en/stable/fields.html
class LoginForm(FlaskForm):
    username = StringField('Usename', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me', validators=[DataRequired()])
    submit = SubmitField('Submit', validators=[DataRequired()])
