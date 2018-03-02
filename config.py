import os

class DevConf(object):
    SWAGGER_Title = "Places API - Development Version"
    SWAGGER_Description = "**DEVELOPMENT VERSION ** This API will allow you to access the information of the places at Georgia Tech. It can be used to find out information about  the offices and the buildings such as their names, addresses, phone numbers, images, categories and GPS coordinates."
    SWAGGER_Host = "dockertest.rnoc.gatech.edu:5000"
    CAS_Server = "https://login.gatech.edu/cas"
    CAS_ValRoute = "/serviceValidate"
    CAS_Secret = "6d4e24b1bbaec5f6f7ac35878920b8ebdfdf71bc53521f31bc4ec47885de610d"  # session secret, does not matter - just a random key.
    SQLA_ConnString = os.environ["DB_CONN"]
    SQLA_DbName = "CORE_gtplaces"
    SQLA_Echo = True
    FLASK_Host = "0.0.0.0"
    FLASK_Port = 5000
    FLASK_Debug = True

class ProdConf(object):
    SWAGGER_Title = "Places API"
    SWAGGER_Description = "This API will allow you to access the information of the places at Georgia Tech. It can be used to find out information about the offices and the buildings such as their names, addresses, phone numbers, images, categories and GPS coordinates."
    SWAGGER_Host = "dockertest.rnoc.gatech.edu:5000"
    CAS_Server = "https://login.gatech.edu/cas"
    CAS_ValRoute = "/serviceValidate"
    CAS_Secret = "6d4e24b1bbaec5f6f7ac35878920b8ebdfdf71bc53521f31bc4ec47885de610d"  # session secret, does not matter - just a random key.
    SQLA_ConnString = os.environ["DB_CONN"]
    SQLA_DbName = "CORE_gtplaces"
    SQLA_Echo = False
    FLASK_Host = "0.0.0.0"
    FLASK_Port = 5000
    FLASK_Debug = False

def get_conf(env="dev"):
    if env == "dev":
        return vars(DevConf)
    elif env == "prod":
        return vars(ProdConf)
    else:
        raise ValueError('Invalid environment name')

