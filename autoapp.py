"""
Application entry point for the Flask CLI

See http://flask.pocoo.org/docs/0.12/cli/

"""
import os

from places import create_app

config_name = os.environ.get("ENV", "development")

# Create the Flask app.
# By convention, the Flask CLI looks for the Flask app to be called 'app'.
app = create_app(config_name)