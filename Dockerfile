FROM alpine:3.7
MAINTAINER Gaurav Ojha gojha@gatech.edu

# update 
RUN apk update && apk upgrade
# install git and python3
RUN apk add python3 git

WORKDIR /app

# 700 permissions is mandatory for Github else it throws error.
	# Host key checking is necessary to avoid the question, "Are you sure you want to add <host> to list of known hosts"
#RUN	chmod 700 /root/.ssh/id_rsa && echo -e "Host github.gatech.edu\n\tStrictHostKeyChecking no\n" >> /root/.ssh/config && \
#    git clone https://github.gatech.edu/gtjourney/gtmobile-gtplaces.git -b docker_api_dev && \
#    && rm -rf /root/.ssh/

# Until can get SSH to work, creating images by adding code present locally, make sure to run docker build from inside the same folder as the code is present.
# this needs to be removed in favor of pulling from GitHub as above

ADD . /app

RUN pip3 install --trusted-host pypi.python.org -r requirements.txt

EXPOSE 5000

CMD ["python3", "places_api.py"]