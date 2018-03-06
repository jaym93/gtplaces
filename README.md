# gtmobile-gtplaces

API for getting campus building information.

Supports the [GT Places web app](https://github.gatech.edu/gtjourney/gtmobile)
of the [m.gatech.edu](https://m.gatech.edu).

## Developer quick start

### How to contribute

Work on all m.gatech.edu-related projects should follow
**[our general contribution guidelines](https://github.gatech.edu/gtjourney/gtmobile/blob/master/CONTRIBUTING.md)**

Before beginning work, **please read the contribution guidelines**.

### Requirements

Requires Python X.XX (TODO)

### Installation for development

TODO: Steps required for
 * setting up the development environment
 * starting a local development instance

### Running tests

TODO: Steps for running unit/integration tests

## OpenAPI / Swagger documentation

TODO: Move Swagger details here

## Deployment for production

TODO: Steps for production deployment

### TODO: Revise the following content from old README:

#### Important
A Dockerfile is a **_must_** for any repositories we are currently migrating. Even if it is not used at the end, with using docker-compose instead, presence of a Dockerfile will greatly help in understanding the dependencies of the application.

#### TODO:
  * Need to fix SSH access to github.gatech.edu for pulling the codebase directly from the repository. Tested with manually adding the source code to the container.
  * Decide on how best to pass the Environment Variables
  * As per the code, the application is running on port 5000, so use the following to start the container (as a daemon)
    
    ```docker run -d -p 5000:5000 -eDB_USERNAME=<DB_USERNAME> -eDB_PASSWORD=<DB_PASSWORD> <image_name>```
    
  * When testing the code you have modified on the server (avoid if at all possible and use git push on development machine, git pull to pull new changes), errors will not be shown by default in the daemon mode. To see error messages, use `-it` option instead of the `-d` option.
    
    Note that we are passing the required environment variables for connecting to the DB service while starting the container. Could be done by mentioning them in the Dockerfile as well. Needs to be decided.


## Development notes
Pretty much the only file you need to modify is places_api.py if you want to modify the behavior of the API. The file contains both the Flask API endpoints and Swagger API documentation in the function documentation of each API call.

The reason to make this a single-file architecture was to ensure documentation and all the relevant parts are updated before any code is changed.

MySQL operations have been replaced by SQLAlchemy ORM. The database structure is defined ORM-style at the beginning, instead of reading from MySQL database at runtime.

API documentation can be accessed from _<url>_/apidocs currently at [http://dockertest.rnoc.gatech.edu:5000/apidocs](http://dockertest.rnoc.gatech.edu:5000/apidocs)

To extract the API spec, use URL _<hostname>_/apispec_1.json, currently at [http://dockertest.rnoc.gatech.edu:5000/apispec_1.json](http://dockertest.rnoc.gatech.edu:5000/apispec_1.json)

Configurations for development and release are stored in conf.py as separate classes, edit them when you need to change any parameter you'd normally need to change. Add other parameters to it as necessary.

## History
In Spring of 2018, this project underwent major changes:
 - API rewritten using Python / Flask
 - Production deployment moved to OpenShift
 - m.gatech.edu web app moved to the [gtmobile repository](https://github.gatech.edu/gtjourney/gtmobile)

 Branches supporting the legacy PHP application have been tagged __legacy/__ for preservation.