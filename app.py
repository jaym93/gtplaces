"""
The app module, containing the app factory function.

Based on Flask Application Factory pattern: http://flask.pocoo.org/docs/patterns/appfactories/

For an example, see https://github.com/sloria/cookiecutter-flask/blob/master/%7B%7Bcookiecutter.app_name%7D%7D/%7B%7Bcookiecutter.app_name%7D%7D/app.py
"""

from flask import Flask

from extensions import cas, swagger
from database import db
from places_api import api


def create_app(config=None):
    """An application factory, as explained here: http://flask.pocoo.org/docs/patterns/appfactories/.

    :param config: The configuration object to use.
    """

    app = Flask(__name__)

    app.config.from_object(config)
    register_extensions(app)
    register_blueprints(app)

    # TODO: create tables if needed. (use command?)
    # # TODO: move creation of SQL Alchemy tables somewhere else
    # if app.config['ENV'] == 'dev':
    #     # create the tables if needed and in dev mode
    #     # don't do this on a production system
    #     metadata.create_all(db)

    return app


def register_extensions(app):
    db.init_app(app)
    cas.init_app(app)
    swagger.init_app(app)


def register_blueprints(app):
    app.register_blueprint(api, url_prefix=app.config["FLASK_BASE_PATH"])
