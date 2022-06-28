# syntax=docker/dockerfile:1
FROM public.ecr.aws/docker/library/python:3.7-stretch

WORKDIR /app
# ADD . /app

RUN apt-get update && \
    apt-get -y install gcc && \
    apt-get install g++ -y && \
    apt-get install unixodbc-dev -y

RUN apt-get install sudo -y && \
    apt-get install curl -y && \
    apt-get install gnupg2 -y

RUN apt-get update && \
    apt-get install -y apt-transport-https && \
    curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add - && \
    curl https://packages.microsoft.com/config/ubuntu/18.04/prod.list > /etc/apt/sources.list.d/mssql-release.list && \
    apt-get update && \
    ACCEPT_EULA=Y apt-get install -y msodbcsql18 && \
    ACCEPT_EULA=Y apt-get install -y mssql-tools 

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt


COPY . .

# CMD [ "python3", "./upload.py" ]