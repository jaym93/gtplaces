import os


class BaseConf(object):
    APP_DIR = os.path.abspath(os.path.dirname(__file__))

    SECRET_KEY = os.environ.get("SECRET_KEY", "change_the_secret_key_in_production")

    CAS_SERVER = os.environ.get("CAS_SERVER", "https://login.gatech.edu/cas")
    CAS_VALIDATE_ROUTE = os.environ.get("CAS_VALIDATE_ROUTE", "/serviceValidate")
    CAS_AFTER_LOGIN = ''
    # TODO: need to add base route?
    SESSION_TYPE = 'filesystem'

    SQLALCHEMY_ECHO = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    SWAGGER_HOST = os.environ.get("SWAGGER_HOST", "0.0.0.0:5000")
    SWAGGER_BASE_PATH = os.environ.get("SWAGGER_BASE_PATH", "/gtplaces")
    # multiple schemes may be space delimited
    SWAGGER_SCHEMES = os.environ.get("SWAGGER_SCHEMES", "http")

    FLASK_BASE_PATH = os.environ.get("FLASK_BASE_PATH", "/gtplaces")


class DevConf(BaseConf):
    ENV = "dev"
    DEBUG = True

    # Using local SQLite DB in project root dir for development
    SQLALCHEMY_DATABASE_NAME = os.environ.get("DB_NAME",'dev.db')
    SQLALCHEMY_DATABASE_PATH = os.path.join(BaseConf.APP_DIR, SQLALCHEMY_DATABASE_NAME)
    SQLALCHEMY_DATABASE_URI = os.environ.get("DB_URL", "sqlite:///{0}".format(SQLALCHEMY_DATABASE_PATH))


class ProdConf(BaseConf):
    ENV = "prod"
    DEBUG = False

    # require that production get critical configuration from environment - no defaults
    # TODO: Production systems should fail immediately if not provided

    # production systems should use a secure, randomly generated secret
    SECRET_KEY = os.environ.get("SECRET_KEY", None)

    SQLALCHEMY_DATABASE_URI = os.environ.get("DB_URL", None)
    SQLALCHEMY_ECHO = False

    SWAGGER_HOST = os.environ.get("SWAGGER_HOST", None)
    SWAGGER_SCHEMES = os.environ.get("SWAGGER_SCHEMES", "https")



def get_conf(env="dev"):
    if env == "dev":
        return DevConf()
    elif env == "prod":
        return ProdConf()
    else:
        raise ValueError('Invalid environment name')


