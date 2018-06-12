FROM python:2
MAINTAINER smartjoe@gmail.com
RUN apt-get update
RUN apt-get install -y python-dev python-setuptools 
RUN apt-get install -y libmariadbclient-dev
RUN easy_install pip 
RUN pip install flask sqlalchemy MySQL-python simplejson
WORKDIR /tidb-workload-simulator
ADD . /tidb-workload-simulator
EXPOSE 9000
ENTRYPOINT python runner 
