# gtmobile-gtplaces
A widget for getting campus building information

## Important
A Dockerfile is a **_must_** for any repositories we are currently migrating. Even if it is not used at the end, with using docker-compose instead, presence of a Dockerfile will greatly help in understanding the dependencies of the application.

## TODO:
  * Need to fix SSH access to github.gatech.edu for pulling the codebase directly from the repository. Tested with manually adding the source code to the container.

### Requirement of a new Branch
This branch ```gtmobile-gtplaces/docker_api_dev``` will only be used for development purposes. 
The aim is to use seperate development and production branches for the duration of our migration to Openshift Origin and to the newer frontend and backend for the application. 

We also aim to have a similar ```docker_api_release``` branch where the working changes will be merged after testing them on the development branch.

Testing this paradigm for gtplaces only currently, and if it works well, will then replicate similar behaviour to all other applications sequentially.
