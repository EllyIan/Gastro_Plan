from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField, DateField,  ValidationError, DateTimeField
from wtforms.validators import DataRequired, Length, Email, EqualTo
import re
from datetime import datetime

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')
    
class UsernameOrEmail:
    def __init__(self, message=None):
        if not message:
            message = 'Invalid email or username.'
        self.message = message

    def __call__(self, form, field):
        if not re.match(r"[^@]+@[^@]+\.[^@]+", field.data) and not re.match(r"^[a-zA-Z0-9_.-]+$", field.data):
            raise ValidationError(self.message)



class LoginForm(FlaskForm):
    #username = StringField('Username', validators=[DataRequired()])
    username_or_email = StringField('Usename or Email', validators=[DataRequired(), UsernameOrEmail()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')

class NewRecipeForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    date = DateField('Date',format='%Y-%m-%d' ,validators=[DataRequired()])
    ingredients = StringField('Ingridients', validators=[DataRequired()])
    instructions = TextAreaField('Instructions', validators=[DataRequired()])
    date_posted = TextAreaField('Date_Posted', validators=[DataRequired()])
    time = TextAreaField('Time', validators=[DataRequired()])
    submit = SubmitField('Create Recipe')
    
'''class MealPlanForm(FlaskForm):
    date = DateField('Date', validators=[DataRequired()])
    breakfast = SelectField('Breakfast', coerce=int)
    lunch = SelectField('Lunch', coerce=int)
    dinner = SelectField('Dinner', coerce=int)
    submit = SubmitField('Create Meal Plan')'''
    
class MealPlanForm(FlaskForm):
    monday_datetime = DateTimeField('Monday Date and Time', format='%Y-%m-%d %H:%M:%S', validators=[DataRequired()], default=lambda: datetime.now())
    monday_breakfast = StringField('Monday Breakfast', validators=[DataRequired()])
    monday_lunch = StringField('Monday Lunch', validators=[DataRequired()])
    monday_dinner = StringField('Monday Dinner', validators=[DataRequired()])

    tuesday_datetime = DateTimeField('Tuesday Date and Time', format='%Y-%m-%d %H:%M:%S', validators=[DataRequired()], default=lambda: datetime.now())
    tuesday_breakfast = StringField('Tuesday Breakfast', validators=[DataRequired()])
    tuesday_lunch = StringField('Tuesday Lunch', validators=[DataRequired()])
    tuesday_dinner = StringField('Tuesday Dinner', validators=[DataRequired()])

    wednesday_datetime = DateTimeField('Wednesday Date and Time', format='%Y-%m-%d %H:%M:%S', validators=[DataRequired()], default=lambda: datetime.now())
    wednesday_breakfast = StringField('Wednesday Breakfast', validators=[DataRequired()])
    wednesday_lunch = StringField('Wednesday Lunch', validators=[DataRequired()])
    wednesday_dinner = StringField('Wednesday Dinner', validators=[DataRequired()])

    thursday_datetime = DateTimeField('Thursday Date and Time', format='%Y-%m-%d %H:%M:%S', validators=[DataRequired()], default=lambda: datetime.now())
    thursday_breakfast = StringField('Thursday Breakfast', validators=[DataRequired()])
    thursday_lunch = StringField('Thursday Lunch', validators=[DataRequired()])
    thursday_dinner = StringField('Thursday Dinner', validators=[DataRequired()])

    friday_datetime = DateTimeField('Friday Date and Time', format='%Y-%m-%d %H:%M:%S', validators=[DataRequired()], default=lambda: datetime.now())
    friday_breakfast = StringField('Friday Breakfast', validators=[DataRequired()])
    friday_lunch = StringField('Friday Lunch', validators=[DataRequired()])
    friday_dinner = StringField('Friday Dinner', validators=[DataRequired()])

    saturday_datetime = DateTimeField('Saturday Date and Time', format='%Y-%m-%d %H:%M:%S', validators=[DataRequired()], default=lambda: datetime.now())
    saturday_breakfast = StringField('Saturday Breakfast', validators=[DataRequired()])
    saturday_lunch = StringField('Saturday Lunch', validators=[DataRequired()])
    saturday_dinner = StringField('Saturday Dinner', validators=[DataRequired()])

    sunday_datetime = DateTimeField('Sunday Date and Time', format='%Y-%m-%d %H:%M:%S', validators=[DataRequired()], default=lambda: datetime.now())
    sunday_breakfast = StringField('Sunday Breakfast', validators=[DataRequired()])
    sunday_lunch = StringField('Sunday Lunch', validators=[DataRequired()])
    sunday_dinner = StringField('Sunday Dinner', validators=[DataRequired()])

    submit = SubmitField('Create Meal Plan')