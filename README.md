# gtmobile-gtplaces

API for getting campus building information.

Supports the [GT Places web app](https://github.gatech.edu/gtjourney/gtmobile)
of [m.gatech.edu](https://m.gatech.edu).
In production at https://m.gatech.edu/api/gtplaces.

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
  (venv)$ export FLASK_APP=autoapp
  (venv)$ export FLASK_DEBUG=true
  ```
  You may want to add this to your `venv/bin/activate` script.
  
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

Run tests via your IDE or with the Flask command:
```
$ flask test
```

### Flask commands

TODO: Document Flask CLI commands
* `flask run`
* `flask create_db_tables`
* `flask test`
* `flask list_routes` - Lists all routes exposed by the Flask application
* `flask shell`

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
  - `ENV=production`
  - `DB_URL` - The full connection URL for the database, including DB scheme, credentials and database name, e.g.
     `mysql+pymysql://USER:PASSWORD@db0.rnoc.gatech.edu/CORE_gtplaces`.  Note that special characters in credentials
     should be URL encoded.
  - `SECRET_KEY` - Use a cryptographic random generator to create a 24 character secret key.  Flask uses this for CAS
    and other crypto.
  - `SWAGGER_HOST` - The public hostname and port of the API in the form `hostname:port`.
  - `SWAGGER_BASE_PATH` - The public base path of the API`, e.g. `/api/gtplaces`
  - `SWAGGER_SCHEMES` - The public schemes supported by the API.  Multiple values may be space delimited,
     e.g. `http https`
  
  See `places/config.py` for additional optional configuration.

### WSGI and Proxy Server
The OpenShift container will serve the app with [Gunicorn, a Python WSGI HTTP Server](http://gunicorn.org/). The
`gunicorn` configuration is provided by `gunicorn_config.py`.

[It is highly recommended that the API lives behind a proxy server.](http://docs.gunicorn.org/en/latest/deploy.html)


## History
In Spring of 2018, this project underwent major changes:
 - API rewritten using Python / Flask
 - Production deployment moved to OpenShift
 - m.gatech.edu web app moved to the [gtmobile repository](https://github.gatech.edu/gtjourney/gtmobile)

 Branches supporting the legacy PHP application have been tagged __legacy/__ for preservation.
