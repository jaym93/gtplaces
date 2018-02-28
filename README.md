# gtmobile-gtplaces
A widget for getting campus building information

## Important
A Dockerfile is a **_must_** for any repositories we are currently migrating. Even if it is not used at the end, with using docker-compose instead, presence of a Dockerfile will greatly help in understanding the dependencies of the application.

## TODO:
  * Need to fix SSH access to github.gatech.edu for pulling the codebase directly from the repository. Tested with manually adding the source code to the container.
  * Decide on how best to pass the Environment Variables
  * As per the code, the application is running on port 5000, so use the following to start the container (as a daemon)
    
    ```docker run -d -p 5000:5000 -eDB_USERNAME=<DB_USERNAME> -eDB_PASSWORD=<DB_PASSWORD> <image_name>```
    
  * When testing the code you have modified on the server (avoid if at all possible and use git push on development machine, git pull to pull new changes), errors will not be shown by default in the daemon mode. To see error messages, use `-it` option instead of the `-d` option.
    
    Note that we are passing the required environment variables for connecting to the DB service while starting the container. Could be done by mentioning them in the Dockerfile as well. Needs to be decided.

### Requirement of a new Branch
This branch ```gtmobile-gtplaces/docker_api_dev``` will only be used for development purposes. 
The aim is to use seperate development and production branches for the duration of our migration to Openshift Origin and to the newer frontend and backend for the application. 

We also have a similar ```docker_api_release``` branch where the working changes will be merged after testing them on the development branch.

Testing this paradigm for gtplaces only currently, and if it works well, will then replicate similar behaviour to all other applications sequentially.

## Notes about the GTPlaces API branch
---
Pretty much the only file you need to modify is places_api.py if you want to modify the behavior of the API. The file contains both the Flask API endpoints and Swagger API documentation in the function documentation of each API call.

The reason to make this a single-file architecture was to ensure documentation and all the relevant parts are updated before any code is changed.

MySQL operations have been replaced by SQLAlchemy ORM. The database structure is defined ORM-style at the beginning, instead of reading from MySQL database at runtime.

API documentation can be accessed from _<url>_/apidocs currently at [http://dockertest.rnoc.gatech.edu:5000/apidocs](http://dockertest.rnoc.gatech.edu:5000/apidocs)

To extract the API spec, use URL _<hostname>_/apispec_1.json, currently at [http://dockertest.rnoc.gatech.edu:5000/apispec_1.json](http://dockertest.rnoc.gatech.edu:5000/apispec_1.json)
