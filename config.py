# config.py
import os

# Enable Flask's debugging features. Should be False in production
DEBUG = True


# DB connection
SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'postgres+psycopg2://webworker:tempPassword@localhost:5432/vmctap'
SQLALCHEMY_TRACK_MODIFICATIONS = False