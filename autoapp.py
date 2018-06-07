"""
Application entry point for the Flask CLI

See http://flask.pocoo.org/docs/0.12/cli/

"""
import os

from api import create_app

# OpenShift's s2i-python-container unsets ENV- use FLASK_ENV as an alternative
config_name = os.environ.get('ENV', os.environ.get('FLASK_ENV', 'development'))

# Create the Flask app.
# By convention, the Flask CLI looks for the Flask app to be called 'app'.
app = create_app(config_name)
