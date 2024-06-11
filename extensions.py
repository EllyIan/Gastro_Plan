from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_migrate import Migrate
from sqlalchemy.orm import sessionmaker
from sqlalchemy import or_

db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = 'auth_routes.login'
login_manager.login_message_category = 'info'
migrate = Migrate()
