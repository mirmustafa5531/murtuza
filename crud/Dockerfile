FROM  python:3

ENV PYTHONUNBUFFERED 1

WORKDIR /app

ADD . /app

COPY ./requirements.txt /app/requrements.txt

RUN pip install -r requirements.txt

COPY .  /app