'''import requests

def get_api_recipe_details(recipe_id, api_key):
    api_url = f"https://api.spoonacular.com/recipes/{recipe_id}/information"
    params = {
        "apiKey": api_key,
        "includeNutrition": False,
    }
    response = requests.get(api_url, params=params)
    response.raise_for_status()  # Raise an exception for non-2xx status codes
    data = response.json()
    recipe_details = data
    return recipe_details '''