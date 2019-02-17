from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError
from app.models import User


class LoginForm(FlaskForm):
    username = StringField('Your username:', validators=[DataRequired()])
    password = PasswordField('Your password:', validators=[DataRequired()])
    remember_me = BooleanField('Remember me')
    submit = SubmitField('Login')


class RegistrationForm(FlaskForm):
    username = StringField('Your username:', validators=[DataRequired()])
    email = StringField('Your email:', validators=[DataRequired(), Email()])
    password = PasswordField('Your password:', validators=[DataRequired()])
    password2 = PasswordField('Repeat password:',
                              validators=[DataRequired(),
                                          EqualTo('password')])
    submit = SubmitField('Register')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Please use different username')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Please use different email')
