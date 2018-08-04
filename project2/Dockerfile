FROM ubuntu:16.04
MAINTAINER Deepak Agrawal
RUN apt-get update
RUN apt-get install -y vim wget git unzip sudo software-properties-common
RUN apt-get install -y python-minimal
RUN apt-get install -y python-pip
#RUN apt-get install -y libpq-dev libxml2-dev libxslt1-dev apt-transport-https
RUN pip install ansible==2.2.0.0

ENV ANSIBLE_HOST_KEY_CHECKING=False
ENV ANSIBLE_ROLES_PATH=/opt/honestbee/project2/roles
ENV ANSIBLE_FORCE_COLOR=true
ENV PATH $PATH:/usr/local/ansible

EXPOSE 80

WORKDIR /opt/honestbee

VOLUME ["/opt/honestbee"]
