"""
Flask extension providing handling of user and app auth from WSO2 API Manager.  Provides function decorators to enforce
auth and retrieve end-user attributes from JSON Web Tokens for endpoints that require auth at the API Manager.  Has
additional support for Georgia Tech GT Accounts.

For more information on WSO2 API Manager support for passing auth data to the API backend, see the WSO2 API Manager
documentation: https://docs.wso2.com/display/AM210/Passing+Enduser+Attributes+to+the+Backend+Using+JWT
"""
from functools import wraps
from http import HTTPStatus

import jwt
from flask import current_app, request, g

JWT_ASSERTION_HEADER = 'X-JWT-Assertion'


"""
Decode the JSON Web Token that WSO2 APIM provides via a the HTTP header 'X-JWT-Assertion'.
"""
def decode_token():
    if JWT_ASSERTION_HEADER in request.headers:
        token = request.headers[JWT_ASSERTION_HEADER]
        # decoded_token = jwt.decode(token, algorithms='RS256')
        return jwt.decode(token, verify=current_app.config['WSO2AUTH_VERIFY_TOKEN'])
    else:
        raise WSO2AuthException("WSO2 authentication is required but request is missing JWT in header "
                                "'X-JWT-Assertion'.  Ensure JWT support is enabled in WSO2 API Manager.")


"""
Flask extension providing handling of user and app auth from WSO2 API Manager.  Provides function decorators to enforce
auth and retrieve end-user attributes from JSON Web Tokens for endpoints that require auth at the API Manager.  Has
additional support for Georgia Tech GT Accounts.
"""
class GTWSO2Auth(object):

    APPLICATION_USER = 'APPLICATION_USER'
    APPLICATION = 'APPLICATION'

    GT_USER_DOMAIN = 'GATECH.EDU'

    def __init__(self, app=None):
        self._app = app
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        app.config.setdefault('WSO2AUTH_VERIFY_TOKEN', False)
        app.config.setdefault('WSO2AUTH_CLAIM_USER_TYPE', 'http://wso2.org/claims/usertype')
        app.config.setdefault('WSO2AUTH_CLAIM_SUBSCRIBER', 'http://wso2.org/claims/subscriber')
        app.config.setdefault('WSO2AUTH_CLAIM_APPLICATION_NAME', 'http://wso2.org/claims/applicationname')
        app.config.setdefault('WSO2AUTH_CLAIM_USERNAME', 'http://wso2.org/claims/username')
        app.config.setdefault('WSO2AUTH_CLAIM_FULL_NAME', 'http://wso2.org/claims/fullname')
        app.config.setdefault('WSO2AUTH_CLAIM_EMAIL_ADDRESS', 'http://wso2.org/claims/emailaddress')
        app.config.setdefault('WSO2AUTH_CLAIM_ENDUSER', 'http://wso2.org/claims/enduser')

        app.teardown_appcontext(self.teardown)

    def teardown(self, exception):
        pass

    @property
    def app(self):
        return self._app or current_app

    """
    Gets the username of the Application User that the API Manager authenticated for the current request.
    """
    @property
    def username(self):
        return g.decoded_token.get(self.app.config['WSO2AUTH_CLAIM_USERNAME']) if g.decoded_token else None

    """
    Returns True if and only if the Application User that the API Manager authenticated for the current request is
    a GT Account.
    """
    @property
    def is_gt_username(self):
        return self.enduser and self.enduser.startswith(self.GT_USER_DOMAIN)

    """
    Gets a list providing the full name of the Application User that the API Manager authenticated for the current 
    request.
    """
    @property
    def full_name(self):
        return g.decoded_token.get(self.app.config['WSO2AUTH_CLAIM_FULL_NAME']) if g.decoded_token else None

    """
    Returns the user type ('Application' or 'Application User') that the API Manager authenticated for the current 
    request.
    """
    @property
    def user_type(self):
        return g.decoded_token.get(self.app.config['WSO2AUTH_CLAIM_USER_TYPE']) if g.decoded_token else None

    """
    Returns the subscriber that the API Manager authenticated for the current request.  The subscriber is the account
    to which the subscribing application belongs.
    """
    @property
    def subscriber(self):
        return g.decoded_token.get(self.app.config['WSO2AUTH_CLAIM_SUBSCRIBER']) if g.decoded_token else None

    """
    Returns the end user that the API Manager authenticated for the current request.  For Application User auth, this
    will be the application user.  For Applicaiton auth, this will be the subscriber.
    """
    @property
    def enduser(self):
        return g.decoded_token.get(self.app.config['WSO2AUTH_CLAIM_ENDUSER']) if g.decoded_token else None

    """
    Returns the decoded JSON Web Token that provides application and application user attributes for the current
    request. 
    """
    @property
    def decoded_token(self):
        return g.decoded_token if g.decoded_token else None

    """
    Decorator for Flask route function for a WSO2 API Manager endpoint that should provide Application auth.  This
    should be configured in the WSO2 APIM's Manage tab for the API. 
    """
    def application_required(self):
        def decorator(f):
            @wraps(f)
            def decorated_function(*args, **kwargs):
                g.decoded_token = decode_token()

                if self.user_type != self.APPLICATION:
                    raise WSO2AuthException("WSO2 authentication token has missing or incorrect usertype claim. This "
                                            "route expects a usertype of APPLICATION.")
                return f(*args, **kwargs)
            return decorated_function
        return decorator

    """
    Decorator for Flask route function for a WSO2 API Manager endpoint that should provide Application User auth.  This
    should be configured in the WSO2 APIM's Manage tab for the API. 
    """
    def application_user_required(self):
        def decorator(f):
            @wraps(f)
            def decorated_function(*args, **kwargs):
                g.decoded_token = decode_token()

                if self.user_type != self.APPLICATION_USER:
                    raise WSO2AuthException("WSO2 authentication token has missing or incorrect usertype claim. This "
                                            "route expects a usertype of APPLICATION_USER.")
                return f(*args, **kwargs)
            return decorated_function
        return decorator

    """
    Decorator for Flask route function for a WSO2 API Manager endpoint that should provide Application or Application
    User auth.  This should be configured in the WSO2 APIM's Manage tab for the API. 
    """
    def application_or_application_user_required(self):
        def decorator(f):
            @wraps(f)
            def decorated_function(*args, **kwargs):
                g.decoded_token = decode_token()

                if self.user_type != self.APPLICATION_USER and self.user_type != self.APPLICATION:
                    raise WSO2AuthException("WSO2 authentication token has missing or incorrect usertype claim. This "
                                            "route expects a usertype of APPLICATION_USER or APPLICATION.")
                return f(*args, **kwargs)
            return decorated_function
        return decorator

    """
    Decorator for Flask route function for a WSO2 API Manager endpoint that should provide Application User auth.  This
    should be configured in the WSO2 APIM's Manage tab for the API. Additionally, this user's account must be a
    GT Account.
    """
    def application_gt_user_required(self):
        def decorator(f):
            @wraps(f)
            def decorated_function(*args, **kwargs):
                # TODO: compose w/ application_user_required rather than repeating code
                g.decoded_token = decode_token()
                if self.user_type != self.APPLICATION_USER:
                    raise WSO2AuthException("WSO2 authentication token has missing or incorrect usertype claim. This "
                                            "route expects a usertype of APPLICATION_USER.")
                if not self.is_gt_username:
                    raise WSO2AuthException("WSO2 authentication token enduser is not a GT Account.", HTTPStatus.UNAUTHORIZED)
                return f(*args, **kwargs)
            return decorated_function
        return decorator


"""
Exception class for WSO2 Auth module.
"""
class WSO2AuthException(Exception):
    status = HTTPStatus.INTERNAL_SERVER_ERROR
    message = 'Internal server error'

    def __init__(self, message=None, status=None):
        Exception.__init__(self)
        if message is not None:
            self.message = message
        if status is not None:
            self.status = status

    def __str__(self):
        return self.message

    def to_dict(self):
        return dict(status=self.status, message=self.message)

