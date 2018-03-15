"""
Application entry point for the Flask CLI

See http://flask.pocoo.org/docs/0.12/cli/

"""
from flask.helpers import get_debug_flag

from places import create_app
from places.config import DevConf, ProdConf

CONFIG = DevConf if get_debug_flag() else ProdConf

# Create the Flask app.
# By convention, the Flask CLI looks for the Flask app to be called 'app'.
app = create_app(CONFIG)