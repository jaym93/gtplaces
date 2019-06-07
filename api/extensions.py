"""
Module for Flask extensions.

Each extension is initialized in the app factory, located in auth.py.
"""
from flasgger import Swagger
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy
# from flask_wso2apim_auth import GTWSO2Auth

db = SQLAlchemy()
ma = Marshmallow()
swagger = Swagger()
# wso2auth = GTWSO2Auth()
