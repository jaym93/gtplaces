"""
Application configuration classes.
"""

import os


class BaseConfig(object):
    APP_DIR = os.path.abspath(os.path.dirname(__file__))
    PROJECT_ROOT = os.path.abspath(os.path.join(APP_DIR, os.pardir))

    FLASK_BASE_PATH = os.environ.get("FLASK_BASE_PATH", None)

    SECRET_KEY = os.environ.get("SECRET_KEY", "change_the_secret_key_in_production")

    CAS_SERVER = os.environ.get("CAS_SERVER", "https://login.gatech.edu/cas")
    CAS_VALIDATE_ROUTE = os.environ.get("CAS_VALIDATE_ROUTE", "/serviceValidate")
    CAS_AFTER_LOGIN = ''
    # TODO: need to add base route?
    SESSION_TYPE = 'filesystem'

    SQLALCHEMY_ECHO = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Swagger config defaults to lazy loading values from the Flask request
    SWAGGER_HOST = os.environ.get("SWAGGER_HOST", "localhost:5000")
    SWAGGER_BASE_PATH = os.environ.get("SWAGGER_BASE_PATH", FLASK_BASE_PATH)
    # multiple schemes may be space delimited: e.g. 'http https'
    SWAGGER_SCHEMES = os.environ.get("SWAGGER_SCHEMES", 'http')
    SWAGGER = {
        "swagger": "2.0",
        "info": {
            "title": "Places API",
            "description": "This API will allow you to access the information of the places at Georgia Tech. It can be"
                           " used to find out information about  the offices and the buildings such as their names, "
                           "addresses, phone numbers, images, categories and GPS coordinates.",
            "contact": {
                "responsibleOrganization": "GT-RNOC",
                "responsibleDeveloper": "RNOC Lab Staff",
                "email": "rnoc-lab-staff@lists.gatech.edu",
                "url": "http://rnoc.gatech.edu/"
            },
            "version": "1.5",
        },

        "host": SWAGGER_HOST,
        # not setting basePath, as flasgger is reading it from the blueprint base path
        "basePath": SWAGGER_BASE_PATH,
        "schemes": SWAGGER_SCHEMES,
        # prefix for the the 'apidocs' endpoint
        "url_prefix": SWAGGER_BASE_PATH
    }


class DevelopmentConfig(BaseConfig):
    DEBUG = True

    # Using local SQLite DB in project root dir for development
    SQLALCHEMY_DATABASE_NAME = os.environ.get("DB_NAME",'dev.db')
    SQLALCHEMY_DATABASE_PATH = os.path.join(BaseConfig.PROJECT_ROOT, SQLALCHEMY_DATABASE_NAME)
    SQLALCHEMY_DATABASE_URI = os.environ.get("DB_URL", "sqlite:///{0}".format(SQLALCHEMY_DATABASE_PATH))


class ProductionConfig(BaseConfig):
    # require that production get critical configuration from environment - no defaults

    # production systems should use a secure, randomly generated secret
    SECRET_KEY = os.environ.get("SECRET_KEY", None)

    # DB_URL Example for MySQL: mysql+pymysql://USER:PASSWORD@db0.rnoc.gatech.edu
    SQLALCHEMY_DATABASE_URI = os.environ.get("DB_URL", None)
    SQLALCHEMY_ECHO = False

    DEBUG = False


class TestConfig(BaseConfig):
    TEST_PATH = os.path.join(BaseConfig.PROJECT_ROOT, 'tests')
    TESTING = True
    DEBUG = False
    SQLALCHEMY_ECHO = False

    # Use in-memory SQLite database for testing
    SQLALCHEMY_DATABASE_URI = 'sqlite://'


# Map configuration name (supplied by the ENV environment variable) to configuration class
CONFIG_NAME_MAP = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'test': TestConfig
}
