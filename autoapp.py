"""
Create an application instance.

Since we are use the Flask Application Factory pattern, the 'flask' CLI needs ann entry point script to create the app.

See http://flask.pocoo.org/docs/0.12/cli/

"""
from flask.helpers import get_debug_flag

from app import create_app
from config import DevConf, ProdConf

CONFIG = DevConf if get_debug_flag() else ProdConf

app = create_app(CONFIG)