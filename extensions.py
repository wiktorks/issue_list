import bcrypt
from flask_mongoengine import MongoEngine
from flask_login import LoginManager
from flask_bcrypt import Bcrypt

mongo = MongoEngine()
bcrypt = Bcrypt()
login_manager = LoginManager()