"""
Initialize the places package.

Based on Flask Application Factory pattern: http://flask.pocoo.org/docs/patterns/appfactories/
"""
from flask import Flask
from places import commands, routes, extensions, errors
from places.config import CONFIG_NAME_MAP
from places.errors import register_error_handlers


def create_app(config_name='development'):
    """
    Create an instance of the Flask application.

    This follows the Flask Application Factory pattern, as explained here:
    http://flask.pocoo.org/docs/patterns/appfactories/

    :param config_name: The name of the configuration
    """

    app = Flask(__name__)

    app.config.from_object(CONFIG_NAME_MAP[config_name])
    register_extensions(app)
    register_blueprints(app)
    register_error_handlers(app)
    register_commands(app)


    return app


def register_extensions(app):
    """Register Flask extensions"""
    extensions.db.init_app(app)
    extensions.ma.init_app(app)
    extensions.cas.init_app(app)
    extensions.swagger.init_app(app)


def register_blueprints(app):
    """Register Flask Blueprints"""
    app.register_blueprint(routes.api, url_prefix=app.config["FLASK_BASE_PATH"])


def register_commands(app):
    """Register Click commands for the Flask CLI"""
    app.cli.add_command(commands.create_db_tables)
    app.cli.add_command(commands.test)
    app.cli.add_command(commands.list_routes)
