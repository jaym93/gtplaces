"""Extensions module. Each extension is initialized in the app factory located in app.py."""
from flasgger import Swagger
from flask_cas import CAS
from flask_sqlalchemy import SQLAlchemy

# TODO
# from places_api import swagger_template

db = SQLAlchemy()
#swagger = Swagger(template=swagger_template)
swagger = Swagger()
cas = CAS()