# gtmobile-gtplaces
A widget for getting campus building information

## Important
A Dockerfile is a **_must_** for any repositories we are currently migrating. Even if it is not used at the end, with using docker-compose instead, presence of a Dockerfile will greatly help in understanding the dependencies of the application.

## TODO:
  * Need to fix SSH access to github.gatech.edu for pulling the codebase directly from the repository. Tested with manually adding the source code to the container.
  * Decide on how best to pass the Environment Variables
  * As per the code, the application is running on port 5000, so use the following to start the container (as a daemon)
    
    ```docker run -d -p 80:5000 -e <DB_USERNAME> -e <DB_PASSWORD> <image_name>```
    
    Note that we are passing the required environment variables for connecting to the DB service while starting the container. Could be done by mentioning them in the Dockerfile as well. Needs to be decided.

### Requirement of a new Branch
This branch ```gtmobile-gtplaces/docker_api_dev``` will only be used for development purposes. 
The aim is to use seperate development and production branches for the duration of our migration to Openshift Origin and to the newer frontend and backend for the application. 

We also aim to have a similar ```docker_api_release``` branch where the working changes will be merged after testing them on the development branch.

Testing this paradigm for gtplaces only currently, and if it works well, will then replicate similar behaviour to all other applications sequentially.
