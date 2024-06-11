from flask import Blueprint, render_template, redirect, url_for, flash, request, jsonify
from flask_login import login_user, logout_user, login_required, current_user
from extensions import db, bcrypt, or_
from models import User, Recipe
from forms import RegistrationForm, LoginForm, NewRecipeForm
from sqlalchemy.exc import IntegrityError
from spoonacular_api import requests, get_api_recipes

auth_routes = Blueprint('auth_routes', __name__)

@auth_routes.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        existing_user = User.query.filter_by(email=form.email.data).first()
        if existing_user:
            flash('Email already exists. Please use a different email.', 'danger')
        else:
            try:
                db.session.add(user)
                db.session.commit()
                flash('Your account has been created!', 'success')
            except IntegrityError:
                db.session.rollback()
                flash('An error occurred. Please try again.', 'danger')
        return redirect(url_for('auth_routes.login'))
    return render_template('register.html', title='Register', form=form)

@auth_routes.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            flash('Login successful!', 'success')
            return redirect(next_page) if next_page else redirect(url_for('main_routes.homepage'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    else:
            flash(' Form not Validated', 'warning')
    return render_template('login.html', title='Login', form=form)

@auth_routes.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.', 'success')
    return redirect(url_for('auth_routes.login'))


main_routes = Blueprint('main_routes', __name__)

@main_routes.route('/')
def landing_page():
    return render_template('landing.html')

@main_routes.route('home')
def homepage():
    return render_template('homepage.html')


recipe_routes = Blueprint('recipe_routes', __name__)

@recipe_routes.route('/recipes', methods=['GET', 'POST'])
@login_required
def manage_recipes():
    form = NewRecipeForm()
    if form.validate_on_submit():
        new_recipe = Recipe(
            title=form.title.data,
            time=form.time.data,
            ingredients=form.ingredients.data,
            instructions=form.instructions.data,
            date_posted=form.date_posted.data,
            user_id=current_user.id
        )
        db.session.add(new_recipe)
        db.session.commit()
        flash('Recipe created successfully!', 'success')
        return redirect(url_for('recipe_routes.manage_recipes'))  # Redirect to the recipe list page
    recipes = Recipe.query.all()
    return render_template('recipe_manager.html', form=form, recipes=recipes)

@recipe_routes.route('/recipe/search', methods=['GET', 'POST'])
@login_required
def search_recipes():
    query = request.args.get('query', '')  # Get the search query from URL parameters
    ingredients = request.args.get('ingredients', '')
    cuisine = request.args.get('cuisine', '')
    diet = request.args.get('diet', '')

    # Search in local database
    local_recipes = Recipe.query.filter(
        or_(
            Recipe.title.ilike(f'%{query}%'),
            Recipe.ingredients.ilike(f'%{query}%'),
            Recipe.instructions.ilike(f'%{query}%'),
        )
    ).all()
    
    local_recipe_data = [{'id': recipe.id, 'title': recipe.title, 'source': 'local'} for recipe in local_recipes]
    
    # Fetch recipes from the Spoonacular API
    api_key = "1e4225ae3f6e4bceac437c9e0f6e097d"  
    api_recipes = get_api_recipes(api_key, query, ingredients, cuisine, diet)
    api_recipe_data = [{'id': recipe['id'], 'title': recipe['title'], 'source': 'api'} for recipe in api_recipes]

    # Combine local and API recipes, prioritizing local recipes
    combined_recipes = local_recipe_data + api_recipe_data

    # Create a new instance of the NewRecipeForm
    form = NewRecipeForm()

    return render_template('recipe_manager.html', query=query, combined_recipes=combined_recipes, form=form)

@recipe_routes.route('/recipe/details/<string:recipe_id>/<string:source>', methods=['GET'])
@login_required
def recipe_details(recipe_id, source):
    if source == "api":
        api_key = "1e4225ae3f6e4bceac437c9e0f6e097d"  #  API key
        api_url = f"https://api.spoonacular.com/recipes/{recipe_id}/information"
        params = {
            "apiKey": api_key,
            "includeNutrition": False
        }
        response = requests.get(api_url, params=params)
        response.raise_for_status()
        recipe = response.json()
        recipe['source'] = 'api'
    elif source == "local":
        recipe = Recipe.query.get(recipe_id)
        recipe.source = 'local'
    else:
        return "Recipe not Found", 400

    # Create a new instance of the NewRecipeForm
    form = NewRecipeForm()

    return render_template('recipe_manager.html', recipe=recipe, form=form)
