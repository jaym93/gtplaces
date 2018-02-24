FROM alpine:3.7
MAINTAINER Gaurav Ojha gojha@gatech.edu

# update 
RUN apk update && apk upgrade
# install git and python3
RUN apk add python3 git

WORKDIR /app

ADD . /app

RUN pip3 install --trusted-host pypi.python.org -r requirements.txt

EXPOSE 5000

CMD ["python3", "places_api.py"]