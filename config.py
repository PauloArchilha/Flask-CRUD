import os


class Config(object):
    basedir = os.path.abspath(os.path.dirname(__file__))


class DevelopmentConfig(object):
    DEVELOPMENT = True
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "sqlite:////" + \
        os.path.join(Config.basedir, "data.sqlite")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    IP_HOST = "localhost"
    PORT_HOST = 3000
