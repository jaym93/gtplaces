import os


class BaseConf(object):
    CAS_SERVER = os.environ.get("CAS_SERVER", "https://login.gatech.edu/cas")
    CAS_VALIDATE_ROUTE = os.environ.get("CAS_VALIDATE_ROUTE", "/serviceValidate")
    # session secret, does not matter - just a random key.
    SECRET_KEY = os.environ.get("SECRET_KEY", "6d4e24b1bbaec5f6f7ac35878920b8ebdfdf71bc53521f31bc4ec47885de610d")

    SQLA_DB_URL = None
    SQLA_ECHO = True

    SWAGGER_HOST = os.environ.get("SWAGGER_HOST", "0.0.0.0:5000")
    SWAGGER_BASE_PATH = os.environ.get("SWAGGER_BASE_PATH", "/")
    # multiple schemes may be space delimited
    SWAGGER_SCHEMES = os.environ.get("SWAGGER_SCHEMES", "http")

    FLASK_HOST = os.environ.get("FLASK_HOST", "0.0.0.0")
    FLASK_PORT = os.environ.get("FLASK_PORT", 5000)
    FLASK_DEBUG = True


class DevConf(BaseConf):
    SQLA_DB_URL = os.environ.get("DB_URL", None) # TODO: Replace with default SQLite DB connection string


class ProdConf(BaseConf):
    # require that production get DB configuration from environment - no defaults
    # TODO: Production should fail immediately if not provided
    SQLA_DB_URL = os.environ.get("DB_URL", None)
    SQLA_ECHO = False

    # TODO: Production should fail immediately if not provided
    SWAGGER_HOST = os.environ.get("SWAGGER_HOST", None)
    SWAGGER_SCHEMES = os.environ.get("SWAGGER_SCHEMES", "https")



def get_conf(env="dev"):
    if env == "dev":
        return DevConf()
    elif env == "prod":
        return ProdConf()
    else:
        raise ValueError('Invalid environment name')

