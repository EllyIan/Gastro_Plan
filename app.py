import os
from flask import Flask
from extensions import db, bcrypt, login_manager, migrate, Migrate
from models import User


app = Flask(__name__)

# Configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///gastro2.db'
app.config['SECRET_KEY'] = 'my_secret_key'

# Initialize extensions
db.init_app(app)
bcrypt.init_app(app)
login_manager.init_app(app)
migrate.init_app(app, db)
migrate = Migrate(app, db)
    
    

# Import and register blueprints
from routes import main_routes
from routes import auth_routes
from routes import recipe_routes

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

app.register_blueprint(main_routes, url_prefix='/')
app.register_blueprint(auth_routes, url_prefix='/auth')
app.register_blueprint(recipe_routes, url_prefix='/recipes')

with app.app_context():
    db.create_all()




if __name__ == '__main__':
    app.run(debug=True)
    