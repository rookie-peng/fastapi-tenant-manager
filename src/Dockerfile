# pull official base image
# FROM python:3.9.4-alpine
FROM registry.rootcloud.com/rootcloud-platform/tenant-manager:base

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# copy requirements file
COPY ./requirements.txt /usr/src/app/requirements.txt

# install dependencies
RUN set -eux \
    && pip install --upgrade pip setuptools wheel \
    && pip install -r /usr/src/app/requirements.txt -i http://pypi.douban.com/simple --trusted-host pypi.douban.com\
    && rm -rf /root/.cache/pip

# copy project
COPY . /usr/src/app/
CMD  uvicorn app.main:app --reload --workers 1 --host 0.0.0.0 --port 9000
