# config.py
from os import environ

# Enable Flask's debugging features. Should be False in production
# ENV = 'development'
# DEBUG = True
# TESTING = True
# TEMPLATES_AUTO_RELOAD = True



# DB connection
# SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'postgres+psycopg2://webworker:tempPassword@localhost:5432/vmctap'
# SQLALCHEMY_DATABASE_URI = "postgres+psycopg2://admin:example@postgredb:5432/vmctap"
# SQLALCHEMY_TRACK_MODIFICATIONS = False


"""Set Flask configuration vars from .env file."""
class Config(object):

    # General Config
    SECRET_KEY = environ.get('SECRET_KEY')
    FLASK_ENV = environ.get('FLASK_ENV')


    # DEBUG FLAGS
    DEBUG = False
    TESTING = False

    # SESSION SETTINGS
    SESSION_COOKIE_NAME = 'session'
    SESSION_COOKIE_SECURE = True
    

    #DATABASE
    # SQLALCHEMY_DATABASE_URI = 
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    DB_DRIVER = environ.get('DB_DRIVER')
    DB_USER = environ.get('DB_USER')
    DB_PASS = environ.get('DB_PASS')
    DB_HOST = environ.get('DB_HOST')
    DB_PORT = environ.get('DB_PORT')
    DB_DATABASE = environ.get('DB_DATABASE')
    DB_URI = environ.get('DB_URI')

    if not DB_URI:
        DB_URI = DB_DRIVER + '://' + DB_USER + ':' + DB_PASS + '@' + DB_HOST + ':' + DB_PORT + '/' + DB_DATABASE

    SQLALCHEMY_DATABASE_URI = DB_URI


class ProdConfig(Config):
    FLASK_ENV = 'production'
    DEBUG = False
    TESTING = False


class DevConfig(Config):
    FLASK_ENV = 'development'
    DEBUG = True
    TESTING = True
    TEMPLATES_AUTO_RELOAD = True

    SESSION_COOKIE_SECURE = False

    SQLALCHEMY_ECHO = True





