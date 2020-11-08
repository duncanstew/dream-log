import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
from dream_blog.config import Config
from flask_wtf.csrf import CSRFProtect

# Setting instance of flask class, __name__ is special vairable that is name of the module. Flask knows hwere to look for templates and static files

db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = 'users.login'
# pass in function name of our route
login_manager.login_message_category = 'info'
# might not work for tailwind
mail = Mail()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)
    csrf = CSRFProtect(app)  

    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)
    csrf.init_app(app)
    # import blueprint objects from each package
    # Have to import routes after the app has been instantiated
    from dream_blog.users.routes import users
    from dream_blog.posts.routes import posts
    from dream_blog.main.routes import main
    from dream_blog.errors.handlers import errors

    app.register_blueprint(users)
    app.register_blueprint(posts)
    app.register_blueprint(main)
    app.register_blueprint(errors)

    # Got rid of app so now we replace all flask imports with a flask method that they have created
    return app

    
