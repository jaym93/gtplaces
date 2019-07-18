"""
API error handling

Provides:
- ApiException classes the API should throw to return an JSON error response and HTTP status code.
- Handlers for Flask-internal HTTP errors that maps to same JSON error response.

Register handlers with `register_error_handlers(app)`
"""

from http import HTTPStatus

from flask.json import jsonify
from werkzeug.exceptions import default_exceptions

#from flask_wso2apim_auth import WSO2AuthException


class ApiException(Exception):
    status = HTTPStatus.INTERNAL_SERVER_ERROR
    message = 'Internal server error'

    def __init__(self, message=None):
        Exception.__init__(self)
        if message is not None:
            self.message = message

    def __str__(self):
        return self.message

    def to_dict(self):
        return dict(status=self.status, message=self.message)


class BadRequestException(ApiException):
    status = HTTPStatus.BAD_REQUEST
    message = 'Bad request'


class UnauthorizedException(ApiException):
    status = HTTPStatus.UNAUTHORIZED
    message = 'Unauthorized'


class ForbiddenException(ApiException):
    status = HTTPStatus.FORBIDDEN
    message = 'Forbidden'


class NotFoundException(ApiException):
    status = HTTPStatus.NOT_FOUND
    message = 'Resource not found'


def handle_api_exception(api_exception):
    """Flask error handler for ApiException.  Register with app.register_error_handler()"""
    return jsonify(api_exception.to_dict()), api_exception.status


def handle_http_error(error):
    """Handle Flask-internal HTTP errors"""
    return jsonify({'message': str(error), 'status': error.code}), error.code


def register_error_handlers(app):
    """Register Flask error handler functions"""
    app.register_error_handler(ApiException, handle_api_exception)
    # app.register_error_handler(WSO2AuthException, handle_api_exception)

    # due to a flask bug in 0.12, we can't handle the default HTTPException.
    # this work-around registers handlers for each status code
    # See: https://github.com/pallets/flask/issues/941
    for code in default_exceptions:
        app.register_error_handler(code, handle_http_error)

