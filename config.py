import os

class DevConf(object):
    SWAGGER_Title = "Places API - Development Version"
    SWAGGER_Description = "**DEVELOPMENT VERSION ** This API will allow you to access the information of the places at Georgia Tech. It can be used to find out information about  the offices and the buildings such as their names, addresses, phone numbers, images, categories and GPS coordinates."
    SWAGGER_Organization = "GT-RNOC"
    SWAGGER_Developer = "Jayanth Mohana Krishna"
    SWAGGER_Email = "jayanth6@gatech.edu"
    SWAGGER_Url = "http://rnoc.gatech.edu/"
    SWAGGER_Host = "dockertest.rnoc.gatech.edu:5000"
    CAS_Server = "https://login.gatech.edu/cas"
    CAS_ValRoute = "/serviceValidate"
    CAS_Secret = "6d4e24b1bbaec5f6f7ac35878920b8ebdfdf71bc53521f31bc4ec47885de610d"
    SQLA_Dialect = "mysql+pymysql://"
    SQLA_Host = "db0.rnoc.gatech.edu:3306"
    SQLA_Username = os.environ["DB_USERNAME"]
    SQLA_Password = os.environ["DB_PASSWORD"]
    SQLA_DbName = "CORE_gtplaces"
    SQLA_ConnString = SQLA_Dialect + SQLA_Username + ':' + SQLA_Password + '@' + SQLA_Host + '/' + SQLA_DbName
    SQLA_Echo = True
    FLASK_Host = "0.0.0.0"
    FLASK_Port = 5000
    FLASK_Debug = True

class ReleaseConf(object):
    SWAGGER_Title = "Places API"
    SWAGGER_Description = "This API will allow you to access the information of the places at Georgia Tech. It can be used to find out information about the offices and the buildings such as their names, addresses, phone numbers, images, categories and GPS coordinates."
    SWAGGER_Organization = "GT-RNOC"
    SWAGGER_Developer = "Jayanth Mohana Krishna"
    SWAGGER_Email = "jayanth6@gatech.edu"
    SWAGGER_Url = "http://rnoc.gatech.edu/"
    SWAGGER_Host = "dockertest.rnoc.gatech.edu:5000"
    CAS_Server = "https://login.gatech.edu/cas"
    CAS_ValRoute = "/serviceValidate"
    CAS_Secret = "6d4e24b1bbaec5f6f7ac35878920b8ebdfdf71bc53521f31bc4ec47885de610d"
    SQLA_Dialect = "mysql+pymysql://"
    SQLA_Host = "db0.rnoc.gatech.edu:3306"
    SQLA_Username = os.environ["DB_USERNAME"]
    SQLA_Password = os.environ["DB_PASSWORD"]
    SQLA_DbName = "CORE_gtplaces"
    SQLA_ConnString = SQLA_Dialect + SQLA_Username + ':' + SQLA_Password + '@' + SQLA_Host + '/' + SQLA_DbName
    SQLA_Echo = False
    FLASK_Host = "0.0.0.0"
    FLASK_Port = 5000
    FLASK_Debug = False

def get_conf(env="dev"):
    if env == "dev":
        return vars(DevConf)
    elif env == "release":
        return vars(ReleaseConf)
    else:
        raise ValueError('Invalid environment name')
