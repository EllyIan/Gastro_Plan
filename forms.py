from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

class LoginForm(FlaskForm):
    #username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')

class NewRecipeForm(FlaskForm):
    title = StringField('title', validators=[DataRequired()])
    time = TextAreaField('Time', validators=[DataRequired()])
    ingredients = StringField('Ingridients', validators=[DataRequired()])
    instructions = TextAreaField('Instructions', validators=[DataRequired()])
    date_posted = TextAreaField('Date_Posted', validators=[DataRequired()])
    submit = SubmitField('Create Recipe')