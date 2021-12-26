import os


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'mysql+pymysql://documationuser:Covid19pass12#@localhost/documation'
    SQLALCHEMY_TRACK_MODIFICATIONS = False