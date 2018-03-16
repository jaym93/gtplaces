"""
Module for Flask extensions.

Each extension is initialized in the app factory, located in __init__.py.
"""
from flasgger import Swagger
from flask_cas import CAS
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
swagger = Swagger()
cas = CAS()