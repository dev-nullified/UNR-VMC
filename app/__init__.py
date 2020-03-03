from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate
from sassutils.wsgi import SassMiddleware
from os import environ


# Globally accessible libraries
db = SQLAlchemy()
ma = Marshmallow()
# r = FlaskRedis()


def create_app():
    """Initialize the core application and load the config."""
    # Initialize the app
    app = Flask(__name__, instance_relative_config=True)
    # app.config.from_object('config')

    # Get config file
    if environ.get("FLASK_ENV").startswith("dev"):
        app.config.from_object("config.DevConfig")
    else:
        app.config.from_object("config.ProdConfig")

    print(f'ENV is set to: {app.config["ENV"]}')

    # Initialize Plugins
    db.init_app(app)
    ma.init_app(app)
    



    with app.app_context():
        # Configure SaaS compile
        app.wsgi_app = SassMiddleware(app.wsgi_app, {
            'app': {
                'sass_path': 'static/styles', 
                'css_path': 'static/css', 
                'wsgi_path': '/static/css', 
                'strip_extension': True
                },
        })


        # DB config
        migrate = Migrate(app, db, compare_type=True)
        # importing the models to make sure they are known to Flask-Migrate
        from .models import person, barcode



        # prevent cached responses
        if app.config["DEBUG"]:
            @app.after_request
            def after_request(response):
                response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate, public, max-age=0"
                response.headers["Expires"] = 0
                response.headers["Pragma"] = "no-cache"
                return response

        # import routes
        from . import views

        return app


# VERY LAST import
# from app import views, models