
FROM python:3.8.1-alpine

# set work directory
WORKDIR /code

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# copy requirements file
COPY ./requirements.txt /code/requirements.txt

# install dependencies
RUN set -eux 
RUN apk add --no-cache --virtual .build-deps build-base \
    libressl-dev libffi-dev gcc musl-dev python3-dev \
    mariadb-dev mysql-client netcat-openbsd\
RUN pip install --upgrade pip setuptools wheel \
RUN pip install -r /code/requirements.txt \
RUN rm -rf /root/.cache/pip

# copy project
COPY . /code
RUN chmod +x ./scripts/wait-for-db.sh
EXPOSE 8080

