import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_login import LoginManager
from flask_bcrypt import Bcrypt

db = SQLAlchemy()
bootstrap = Bootstrap()
login_manager = LoginManager()
login_manager.login_view = 'authentication.do_the_login'
login_manager.session_protection = 'strong'
bcrypt = Bcrypt()

def create_app(config_type):
    # declarations
    app = Flask(__name__)
    configuration = os.path.join(os.getcwd(), 'config', config_type + '.py')
    app.config.from_pyfile(configuration)

    # start up on various packages
    db.init_app(app)
    bootstrap.init_app(app)
    login_manager.init_app(app)
    bcrypt.init_app(app)

    # pulling in the Blueprints
    from app.character import main
    app.register_blueprint(main)

    from app.compendium import compend
    app.register_blueprint(compend)

    from app.auth import authentication
    app.register_blueprint(authentication)

    return app
