# gtmobile-gtplaces

API for getting campus building information.

Supports the [GT Places web app](https://github.gatech.edu/gtjourney/gtmobile)
of [m.gatech.edu](https://m.gatech.edu).
In production at https://m.gatech.edu/api/gtplaces.

**PLEASE NOTE: wso2 authentication has been removed due to this API being moved to a new OpenShift cluster. Endpoints that allow "writes" are also removed, due to removal of authentication.**

## Development

### How to contribute

Work on all m.gatech.edu-related projects should follow
**[our general contribution guidelines](https://github.gatech.edu/gtjourney/gtmobile/blob/master/CONTRIBUTING.md)**

Before beginning work, **please read the contribution guidelines**.

### Prerequisites

##### Python and pip
Ensure you have the latest version of [Python 3](https://www.python.org/downloads/) (>=3.6) and 
[pip](https://packaging.python.org/key_projects/#pip) and that both are available from the command line  You can check this
by running:
```
$ python --version
$ pip --version
```

##### Virtualenv
It's highly recommended that you use [Virtualenv](https://virtualenv.pypa.io/en/latest/) during development.  For a
breif overview of how to work with Virtualenv and the Flask CLI, check out the 
[Flask installation guide](http://flask.pocoo.org/docs/0.12/installation/#virtualenv).  To install:

```
$ sudo pip install virtualenv
```

##### A good Python IDE
Using an IDE like [PyCharm](https://www.jetbrains.com/pycharm) is recommended and [free for student use](https://www.jetbrains.com/student/).
Among other benefits, the built in code analysis can help you write better code.


### Developer quick start

* Clone the repository
  ```
  $ git clone https://github.gatech.edu/gtjourney/gtmobile-gtplaces.git
  $ cd gtmobile-gtplaces
  ```
  
* Set up virtualenv
  ``` 
  $ virtualenv -p python3 venv
  $ source venv/bin/activate
  ```
  
* Install requirements
  ```
  (venv)$ pip install -r requirements.txt
  ```
  
* Set environment variables required by the `flask` CLI
  ```
  (venv)$ export FLASK_APP=autoapp.py
  (venv)$ export FLASK_DEBUG=true
  ```
  You may want to add this to your `venv/bin/activate` script.
  
  If your `flask` commands fail after setting `FLASK_APP=autoapp`, try using the absolute path to `autoapp.py`.
  
* Setup your development SQLite database

  You may either use the provided `sample.db`
  ```
  (venv)$ cp sample.db dev.db
  ```
  or initialize an empty database
  ```
  (venv)$ flask create_db_tables
  ```
  
* Run it!
  ```
  (venv)$ flask run
   * Serving Flask app "autoapp"
   * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
  ```
  You may also specify the host and port: `flask run -h localhost -p 8080`
  
  Point a web browser to [http://localhost:5000/apidocs](http://localhost:5000/apidocs) to test drive!

* Run in your IDE

  PyCharm 2018 supports executing with `flask run` out of the box.  For earlier version of PyCharm
  or other IDEs, see [these configuration steps from the Flask docs](https://github.com/pallets/flask/blob/master/docs/cli.rst)


### Local development database

For development, Sequel Alchemy is configured by default to use a local SQLite database, `dev.db`, which is ignored by Git.

The provided `sample.db` contains a dump of the production database as of 3/18/2018.  To use this sample data for
development, copy `sample.db` and rename to `dev.db`.

##### How to create a SQLite sample database

To create this sample database, [this MySQL to SQLite recipe](http://livecode.byu.edu/database/mysql-sqliteExport.php)
was used.  Other scripts such as [dumblob/mysql2sqlite](https://github.com/dumblob/mysql2sqlite) may also be useful.

In this case, the entire DB was dumped as it was fairly small--  for other projects with large databases, you may only
need to export a subset of an existing database, or alternatively you can generate mock data for development.

Ultimately, you should be testing against test fixtures which you should probably define in your test scripts.

### Running tests

Run [pytest](https://docs.pytest.org/en/latest/) unit / integration tests via your IDE or with the Flask command:
```
$ flask test
```

### Flask commands

The [Flask Command Line Interface](http://flask.pocoo.org/docs/0.12/cli/) is used to run the API in development mode,
execute automated tests and perform other development-related tasks.  In addition to the built in commands, custom
commands are implemented in `api/commands.py`.

* **`flask run`** - Starts the API using Flask's built-in web server. This is not intended for production!
* **`flask create_db_tables`** - Creates database tables if needed, using the DB provided by the current configuration.
  To change the DB, see configuration options in `api/config.py`
* **`flask test`** - Executes automated tests using [pytest](https://docs.pytest.org/en/latest/).
* **`flask list_routes`** - Lists all routes exposed by the Flask application
* **`flask shell`** - Starts [Flask's interactive shell](http://flask.pocoo.org/docs/0.12/shell/).

Getting a `flask: command not found` error? Ensure that you've set `export FLASK_APP=autoapp`.

## OpenAPI / Swagger specification

We use [OpenAPI Specification](https://github.com/OAI/OpenAPI-Specification)
(aka Swagger Specification) to specify and document the API.
This machine readable documentation can be used to generate interactive
documentation, client implementations, test suites and perform other
useful functions.

Our OpenAPI spec is authored is authored as inline Python docstring rather
than an external YAML or JSON file to ease the process of and improve the
 likelihood of keeping the spec and source code in sync.

The API reclies on the [flasgger](https://github.com/rochacbruno/flasgger)
library, which extracts our inline OpenAPI Spec to provide interactive
documentation via [Swagger UI](https://swagger.io/swagger-ui/),
perform request validation, and generate stand-alone OpenAPI Spec files.

#### Interactive API documentation - Swagger UI

To access interactive [Swagger UI](https://swagger.io/swagger-ui/)
documentation, point a browser to:
```
<API_URL>/apidocs
```

#### Extracting an OpenAPI Specification file

To exract an OpenAPI Specification JSON file, point a browser to:
```
<API_URL>/apispec_1.json
```

## Production deployment

### OpenShift
Deployment to OpenShift is supported with [OpenShift Source-to-Image](https://github.com/openshift/source-to-image),
or S2I. For implementation details, see the [OpenShift Python S2I Container](https://github.com/sclorg/s2i-python-container).

When creating an OpenShift application:
* From _Add to project_, choose `python:3.5` or later.
* Set the required environment variables:
  - `DB_URL` - The full connection URL for the database, including DB scheme, credentials and database name, e.g.
     `mysql+pymysql://USER:PASSWORD@db0.rnoc.gatech.edu/CORE_gtplaces`.  Note that special characters in credentials
     should be URL encoded.
  - `SECRET_KEY` - Use a cryptographic random generator to create a 24 character secret key. Flask uses this value
     for internal crypto operations which should not be required by this API, but change from the default to ensure
     security.
  
  See `api/config.py` for additional optional configuration. 
  
  Note that unchanging environment variables (e.g. `FLASK_ENV=production`) are set in `.s2i/environment` file.

#### Local development using the OpenShift S2I container

For development / debugging of issues related to production deployment, the 
[OpenShift Python S2I Container](https://github.com/sclorg/s2i-python-container) can be run locally in Docker.  This is
is much faster than deploying a development build to OpenShift and will avoid consumption of server resources.

* Install [Source-to-Image](https://github.com/openshift/source-to-image).  
* Create a local file with environment variables that would be configured in OpenShift (use a `.env` extension
  and this file will be ignored by git):
  ```
  SECRET_KEY=used_by_flask-no_need_to_change
  DB_URL=mysql+pymysql://CHANGE_THIS_USER_NAME:CHANGE_THIS_PASSWORD@db0.rnoc.gatech.edu/CORE_gtplaces
  ```
* Build the image.  From a command prompt open to the source directory:
  ```
  $ s2i build . centos/python-36-centos7 gtplaces -E my.enviroment.variables.env
  ``` 
  
* Run the container:
  ```
  $ docker run -p 8080:8080 gtplaces
  ```
  This will run the container with the source code that was built into the image.  
  
  We can also volume mount the source code and changes will be hot deployed.  This is probably what you want to do for \
  development.
  ```
  $ docker run -p 8080:8080 -v /YOUR/LOCAL/SOURCE/PATH:/opt/app-root/src gtplaces
  ```
  
#### WSGI and Proxy Server
The OpenShift container will serve the app with [Gunicorn, a Python WSGI HTTP Server](http://gunicorn.org/). The
`gunicorn` configuration is provided by `gunicorn_config.py`.

[It is highly recommended that the API lives behind a proxy server.](http://docs.gunicorn.org/en/latest/deploy.html)

### WSO2 API Manager
The API is designed to execute behind WSO2 API Manager, an API gateway.

#### Consuming the API:
Subscribe to the API through the API Store: https://portal.api.rnoc.gatech.edu/store

#### Publishing changes to the API:
* Changes to the API must be published to the WSO2 API Manager via the Publisher portal:
  https://portal.api.rnoc.gatech.edu/publisher
* Changes must be made using WSO2 APIM account owning the API: `rnoclabstaff`
* API changes will require updating the Open API spec in the Publisher portal. See 
  [Extracting an OpenAPI Specification file](#Extracting-an-OpenAPI-Specification-file).
* When changing the API, changes should always be published using a new version number.

## History
In Spring of 2018, this project underwent major changes:
 - API rewritten using Python / Flask
 - Production deployment moved to OpenShift, with WSO2 API Manager as an API gateway
 - m.gatech.edu web app moved to the [gtmobile repository](https://github.gatech.edu/gtjourney/gtmobile)

 Branches supporting the legacy PHP application have been tagged __legacy/__ for preservation.
