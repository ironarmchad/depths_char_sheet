import os
from flask import Flask
from flask_bootstrap import Bootstrap

bootstrap = Bootstrap()


def create_app(config_type):
    # declarations
    app = Flask(__name__)
    configuration = os.path.join(os.getcwd(), 'config', config_type + '.py')
    app.config.from_pyfile(configuration)

    # start up on various packages
    bootstrap.init_app(app)

    # pulling in the Blueprints
    from app.character import main
    app.register_blueprint(main)

    return app
