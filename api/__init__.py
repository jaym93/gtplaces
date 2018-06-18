"""
Initialize the places package.

Based on Flask Application Factory pattern: http://flask.pocoo.org/docs/patterns/appfactories/
"""
import logging

from flask import Flask
from api import commands, routes, extensions, errors
from api.config import CONFIG_NAME_MAP
from api.errors import register_error_handlers


def create_app(config_name='development'):
    """
    Create an instance of the Flask application.

    This follows the Flask Application Factory pattern, as explained here:
    http://flask.pocoo.org/docs/patterns/appfactories/

    :param config_name: The name of the configuration
    """

    app = Flask(__name__)

    app.config.from_object(CONFIG_NAME_MAP[config_name])
    configure_logger(app)
    register_extensions(app)
    register_blueprints(app)
    register_error_handlers(app)
    register_commands(app)

    # NOTE: In debug mode, Flask may create app twice, resulting in duplicate log output
    # In production, gunicorn will run multiple processes, creating multiple Flask apps
    app.logger.info('Flask app created with configuration: %s', config_name)

    return app


def configure_logger(app):
    if app.config['ENV'] == 'production':
        # if running within the production gunicorn WGSI server, wire flask's logger to gunicorn log handlers
        gunicorn_logger = logging.getLogger('gunicorn.error')
        app.logger.handlers = gunicorn_logger.handlers
        # set Flask log level to match the level set for gunicorn
        app.logger.setLevel(gunicorn_logger.level)


def register_extensions(app):
    """Register Flask extensions"""
    extensions.db.init_app(app)
    extensions.ma.init_app(app)
    extensions.swagger.init_app(app)
    extensions.wso2auth.init_app(app)


def register_blueprints(app):
    """Register Flask Blueprints"""
    app.register_blueprint(routes.api, url_prefix=app.config["FLASK_BASE_PATH"])


def register_commands(app):
    """Register Click commands for the Flask CLI"""
    app.cli.add_command(commands.create_db_tables)
    app.cli.add_command(commands.test)
    app.cli.add_command(commands.list_routes)
