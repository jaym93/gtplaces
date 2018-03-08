import os


class BaseConf(object):
    SWAGGER_Title = "Places API - Development Version"
    SWAGGER_Description = "This API will allow you to access the information of the places at Georgia Tech. It can be used to find out information about  the offices and the buildings such as their names, addresses, phone numbers, images, categories and GPS coordinates."
    SWAGGER_Host = os.environ.get("SWAGGER_HOST", "dockertest.rnoc.gatech.edu:5000")

    CAS_Server = os.environ.get("CAS_SERVER", "https://login.gatech.edu/cas")
    CAS_ValidateRoute = "/serviceValidate"
    CAS_Secret = "6d4e24b1bbaec5f6f7ac35878920b8ebdfdf71bc53521f31bc4ec47885de610d"  # session secret, does not matter - just a random key.

    SQLA_DbUrl = None
    SQLA_Echo = True

    FLASK_Host = os.environ.get("FLASK_HOST", "0.0.0.0")
    FLASK_Port = os.environ.get("FLASK_PORT", 5000)
    FLASK_Debug = True


class DevConf(BaseConf):
    SQLA_DbUrl = os.environ.get("DB_URL", None) # TODO: Replace with default SQLite DB connection string


class ProdConf(BaseConf):
    # require that production get DB configuration from environment - no defaults
    SQLA_DbUrl = os.environ["DB_URL"]
    SQLA_Echo = False

    FLASK_Debug = False


def get_conf(env="dev"):
    if env == "dev":
        return DevConf()
    elif env == "prod":
        return ProdConf()
    else:
        raise ValueError('Invalid environment name')

