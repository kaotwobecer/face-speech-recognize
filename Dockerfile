FROM python:3.6

ENV PYTHONUNBUFFERED=1

COPY requirements.txt requirements.txt

RUN pip install --upgrade pip setuptools && pip install -r requirements.txt \
    && apt-get update \
    && apt-get upgrade -y \
    && apt-get -y install apt-utils gcc libpq-dev libsndfile-dev
    
COPY . .