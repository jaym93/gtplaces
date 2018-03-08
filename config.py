import os


class BaseConf(object):
    CAS_Server = os.environ.get("CAS_SERVER", "https://login.gatech.edu/cas")
    CAS_ValidateRoute = os.environ.get("CAS_VALIDATE_ROUTE", "/serviceValidate")
    # session secret, does not matter - just a random key.
    CAS_Secret = os.environ.get("SECRET_KEY", "6d4e24b1bbaec5f6f7ac35878920b8ebdfdf71bc53521f31bc4ec47885de610d")

    SQLA_DbUrl = None
    SQLA_Echo = True

    SWAGGER_Host = os.environ.get("SWAGGER_HOST", "0.0.0.0:5000")
    SWAGGER_BasePath = os.environ.get("SWAGGER_BASE_PATH", "/")
    # multiple schemes may be space delimited
    SWAGGER_Schemes = os.environ.get("SWAGGER_SCHEMES", "http")

    FLASK_Host = os.environ.get("FLASK_HOST", "0.0.0.0")
    FLASK_Port = os.environ.get("FLASK_PORT", 5000)
    FLASK_Debug = True


class DevConf(BaseConf):
    SQLA_DbUrl = os.environ.get("DB_URL", None) # TODO: Replace with default SQLite DB connection string


class ProdConf(BaseConf):
    # require that production get DB configuration from environment - no defaults
    # TODO: Production should fail immediately if not provided
    SQLA_DbUrl = os.environ.get("DB_URL", None)
    SQLA_Echo = False

    # TODO: Production should fail immediately if not provided
    SWAGGER_Host = os.environ.get("SWAGGER_HOST", None)

    SWAGGER_Scheme = os.environ.get("SWAGGER_SCHEMES", "https")



def get_conf(env="dev"):
    if env == "dev":
        return DevConf()
    elif env == "prod":
        return ProdConf()
    else:
        raise ValueError('Invalid environment name')

