"""
Application entry point for the Flask CLI

See http://flask.pocoo.org/docs/0.12/cli/

"""
import os

from api import create_app

# DEBUG for OpenShift issue
for key in os.environ.keys():
    print("%30s %s \n" % (key,os.environ[key]))

config_name = os.environ.get("ENV", "development")

# Create the Flask app.
# By convention, the Flask CLI looks for the Flask app to be called 'app'.
app = create_app(config_name)
