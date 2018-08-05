FROM ubuntu:16.04
MAINTAINER Deepak Agrawal
RUN apt-get update --fix-missing
RUN apt-get install -y vim curl sudo
RUN apt-get install -y python-minimal
RUN apt-get install -y python-pip apache2-utils
RUN pip install --upgrade pip
#RUN apt-get install -y libpq-dev libxml2-dev libxslt1-dev apt-transport-https
RUN pip install ansible==2.2.0.0
RUN pip install boto
RUN pip install boto3

ENV ANSIBLE_HOST_KEY_CHECKING=False
ENV ANSIBLE_ROLES_PATH=/opt/honestbee/project2/roles
ENV ANSIBLE_FORCE_COLOR=true
ENV PATH $PATH:/usr/local/ansible

EXPOSE 80

WORKDIR /opt/honestbee/project2

VOLUME ["/opt/honestbee"]
CMD ["ansible-playbook", "-u", "ubuntu", "site.yml"]
#CMD ["ab", "-n", "100", "-c", "10", "http://localhost/"]
