from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from sassutils.wsgi import SassMiddleware

# Initialize the app
app = Flask(__name__, instance_relative_config=True)


# Load the config file
app.config.from_object('config')

# Configure SaaS compile
app.wsgi_app = SassMiddleware(app.wsgi_app, {
    'app': ('static/styles', 'static/css', '/static/css')
})

# DB config
db = SQLAlchemy(app)
migrate = Migrate(app, db)


# prevent cached responses
if app.config["DEBUG"]:
    @app.after_request
    def after_request(response):
        response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate, public, max-age=0"
        response.headers["Expires"] = 0
        response.headers["Pragma"] = "no-cache"
        return response

# VERY LAST import
from app import views, models