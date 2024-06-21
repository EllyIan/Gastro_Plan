# GastroPlan: Your Personalized Meal Planning Companion

GastroPlan is a comprehensive web application designed to simplify meal planning and recipe management. It provides users with personalized meal plans, ingredient substitutions, and shopping lists, all tailored to their dietary preferences and restrictions.

## Table of Contents

- [Features](#features)
- [Technologies](#technologies)
- [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Project Status](#project-status)
- [Challenges](#challenges)
- [Collaboration](#collaboration)
- [Contributing](#contributing)
- [License](#license)

## Features

- **Drag-and-Drop Meal Planner**: Organize meals in a calendar-based planner.
- **Meal Plan Templates**: Quick start with pre-made templates for specific diets or weekly themes.
- **Substitution Suggestions**: Alternative ingredient suggestions for unavailable items.
- **Grouped Shopping Lists**: Organized by categories for efficient shopping.
- **User Preferences Storage**: Save dietary restrictions, preferred cuisines, and ingredient preferences.
- **Customized Recipe Suggestions**: Personalized recommendations based on user preferences.
- **Allergen Alerts**: Warnings for recipes containing allergens.
- **Preparation Time Filter**: Filter recipes based on available time.
- **Quick Meal Recommendations**: Recipes with shorter preparation times.
- **Local Shop Integration**: Suggest local shops for ingredients.
- **Random Recipe Generator**: Discover new dishes with the "Surprise Me" button.
- **Customizable Surprise Suggestions**: Random suggestions aligned with user tastes.
- **Recipe Suggestions by Mood**: Match recipes to user cravings.

## Technologies

- **Backend**: Python, Flask, SQLAlchemy
- **Frontend**: HTML, CSS, Bootstrap
- **Database**: MongoDB
- **Infrastructure**: Custom server

## Installation

### Prerequisites

- Python 3.8+
- MongoDB
- Flask

### Setup

1. Clone the repository:
    ```bash
    git clone https://github.com/EllyIan/gastroplan.git
    cd gastroplan
    ```

2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Set up the database:
    ```python
    from app import db
    db.create_all()
    ```

4. Run the application:
    ```bash
    flask run
    ```

## Usage

- **Login**: Access the app by logging in with your credentials.
- **Meal Planner**: Use the drag-and-drop interface to organize your meals.
- **Recipe Creation**: Add new recipes and specify ingredient substitutions.
- **Shopping Lists**: Generate categorized shopping lists from your meal plans.

## API Endpoints

- **GET /api/recipes**: Retrieve all recipes or filtered by parameters.
- **POST /api/recipes**: Create a new recipe.
- **PUT /api/recipes/{id}**: Update a specific recipe by ID.
- **DELETE /api/recipes/{id}**: Delete a recipe by ID.
- **GET /api/meal-plans**: Retrieve all meal plans or filtered by parameters.
- **POST /api/meal-plans**: Create a new meal plan.

## Project Status

### Progress

- Scale of Progress: 7/10
- **Completed**:
  - Backend setup
  - MongoDB integration
  - Basic user authentication
  - Frontend design
- **In Progress**:
  - API integration for fetching and displaying recipes
  - Drag-and-drop meal planner
  - Recipe details view

### Challenges

- **Technical**: API integration issues and detailed recipe view errors.
- **Non-Technical**: Time management and scheduling.

### Collaboration

- Effective use of GitHub and version control.
- Regular stand-up meetings and brainstorming sessions.
- Asynchronous communication tools for flexible collaboration.

## Contributing

Contributions are welcome! Please fork the repository and create a pull request with your changes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
