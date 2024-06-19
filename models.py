from datetime import datetime
from extensions import db
from flask_login import UserMixin
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey



class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)
    recipes = db.relationship('Recipe', backref='author', lazy=True)
    
    meal_plans = relationship('MealPlan', back_populates='user')
    recipes = relationship('Recipe', back_populates='user')
    
    @staticmethod
    def get_by_id(user_id):
        return User.query.get(int(user_id))

class Recipe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    time = db.Column(db.String(20), nullable=True)
    ingredients = db.Column(db.Text, nullable=False)
    instructions = db.Column(db.Text, nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    
    user = relationship('User', back_populates='recipes')
    
class MealPlan(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, nullable=False)
    breakfast_id = db.Column(db.Integer, db.ForeignKey('recipe.id'), nullable=True)
    lunch_id = db.Column(db.Integer, db.ForeignKey('recipe.id'), nullable=True)
    dinner_id = db.Column(db.Integer, db.ForeignKey('recipe.id'), nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    
    breakfast = db.relationship('Recipe', foreign_keys=[breakfast_id])
    lunch = db.relationship('Recipe', foreign_keys=[lunch_id])
    dinner = db.relationship('Recipe', foreign_keys=[dinner_id])
    user = db.relationship('User', back_populates='meal_plans')