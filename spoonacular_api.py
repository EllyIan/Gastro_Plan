# spoonacular_api.py

import requests

import requests

def get_api_recipes(api_key, query=None, ingredients=None, cuisine=None, diet=None):
    api_url = "https://api.spoonacular.com/recipes/complexSearch"
    params = {
        "apiKey": api_key,
        "query": query,
        "includeIngredients": ingredients,
        "cuisine": cuisine,
        "diet": diet,
        "addRecipeInformation": True,
        "number": 10
    }
    response = requests.get(api_url, params=params)
    response.raise_for_status()
    data = response.json()
    recipes = data.get("results", [])
    return recipes
