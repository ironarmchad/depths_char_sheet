from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField
from wtforms.validators import DataRequired, Length, EqualTo


class RegistrationForm(FlaskForm):
    username = StringField("Username",
                           validators=[DataRequired(), Length(3, 30, message='Between 3 to 30 characters')])
    password = PasswordField('Password',
                             validators=[DataRequired(), Length(5, 30, message='Between 5 and 30 characters'),
                                         EqualTo('confirm', message='passwords must match')])
    confirm = PasswordField('Confirm', validators=[DataRequired()])
    submit = SubmitField('Register')


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    stay_logged_in = BooleanField('stay logged-in')
    submit = SubmitField()
