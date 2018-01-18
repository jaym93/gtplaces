# Dockerfile to deploy Python services to dockertest.rnoc.gatech.edu

FROM ubuntu
MAINTAINER Jayanth Mohana Krishna "jayanthm@gatech.edu"

# Port to expose
EXPOSE 5000

# Arguments
ARG repo # the git repo we will be pulling from
ARG service # the name of the API (like gtplaces or gtpower)

# Base update
RUN apt-get update && apt-get -y upgrade

# Install required packages
RUN apt-get isntall python3 python3-pip
RUN apt-get install build-tools
RUN apt-get install git

# Install Python packages
RUN pip3 install flask
RUN pip3 install pymysql

# Get the CAS authenticator for Flask
RUN git clone git@github.com:cameronbwhite/Flask-CAS.git
RUN cd Flask-CAS
RUN python3 setup.py install
RUN cd ..

# Get the python server from github
RUN git clone #...github.gatech.edu URL here

# Run the service
CMD ["python","./app.py"]
