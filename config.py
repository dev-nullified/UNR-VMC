# config.py
import os

# Enable Flask's debugging features. Should be False in production
DEBUG = True


# DB connection
SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'postgres+psycopg2://postgres:password@localhost:5432/VMCTAP'
SQLALCHEMY_TRACK_MODIFICATIONS = False