"""
Initialize the places package.

Based on Flask Application Factory pattern: http://flask.pocoo.org/docs/patterns/appfactories/
"""
from flask import Flask
from places import commands, routes, extensions


def create_app(config=None):
    """
    Create an instance of the Flask application.

    This follows the Flask Application Factory pattern, as explained here:
    http://flask.pocoo.org/docs/patterns/appfactories/

    :param config: The configuration object to use.
    """

    app = Flask(__name__)

    app.config.from_object(config)
    register_extensions(app)
    register_blueprints(app)
    register_commands(app)

    return app


def register_extensions(app):
    """Register Flask extensions"""
    extensions.db.init_app(app)
    extensions.cas.init_app(app)
    extensions.swagger.init_app(app)


def register_blueprints(app):
    """Register Flask Blueprints"""
    app.register_blueprint(routes.api, url_prefix=app.config["FLASK_BASE_PATH"])


def register_commands(app):
    """Register Click commands for the Flask CLI"""
    app.cli.add_command(commands.create_db_tables)
