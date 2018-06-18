"""
Application configuration classes.
"""

import os


class BaseConfig(object):
    APP_DIR = os.path.abspath(os.path.dirname(__file__))
    PROJECT_ROOT = os.path.abspath(os.path.join(APP_DIR, os.pardir))

    # Base path of the API - Typically not set, as the API is behind a reverse proxy / API gateway
    FLASK_BASE_PATH = os.environ.get("FLASK_BASE_PATH", None)

    # Secret used by Flask for crypto - not actually used by this API, but change from default to be secure
    SECRET_KEY = os.environ.get("SECRET_KEY", "change_the_secret_key_in_production")

    # Swagger / Open API Specification configuration
    # Swagger config defaults to lazy loading values from the Flask request
    SWAGGER = {
        "swagger": "2.0",
        "info": {
            "title": "GT Places API",
            "description": "Provides information on buildings and locations on the Georgia Tech campus, including "
                           "address, contact information, images, geocoordinates and more.",
            # Version of our API
            "version": "1.5",
        },
        # prefix for the the '/apidocs' endpoint
        "url_prefix": FLASK_BASE_PATH
    }

    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(BaseConfig):
    DEBUG = True

    # Using local SQLite DB in project root dir for development
    SQLALCHEMY_DATABASE_NAME = os.environ.get("DB_NAME",'dev.db')
    SQLALCHEMY_DATABASE_PATH = os.path.join(BaseConfig.PROJECT_ROOT, SQLALCHEMY_DATABASE_NAME)
    SQLALCHEMY_DATABASE_URI = os.environ.get("DB_URL", "sqlite:///{0}".format(SQLALCHEMY_DATABASE_PATH))
    SQLALCHEMY_ECHO = True


class ProductionConfig(BaseConfig):
    DEBUG = False

    # require that production get critical configuration from environment - no defaults

    # production systems should use a secure, randomly generated secret
    SECRET_KEY = os.environ.get("SECRET_KEY", None)

    # DB_URL Example for MySQL: mysql+pymysql://USER:PASSWORD@db0.rnoc.gatech.edu
    SQLALCHEMY_DATABASE_URI = os.environ.get("DB_URL", None)


class TestConfig(BaseConfig):
    TEST_PATH = os.path.join(BaseConfig.PROJECT_ROOT, 'tests')
    TESTING = True
    DEBUG = False

    # Use in-memory SQLite database for testing
    SQLALCHEMY_DATABASE_URI = 'sqlite://'

    # disable verification of WSO2 auth token during testing
    WSO2AUTH_VERIFY_TOKEN = False


# Map configuration name (supplied by the ENV environment variable) to configuration class
CONFIG_NAME_MAP = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'test': TestConfig
}
