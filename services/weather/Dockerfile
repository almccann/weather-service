FROM python:3.7-alpine

COPY weather.txt requirements.txt

ENV FLASK_APP app.py
ENV FLASK_RUN_HOST 0.0.0.0
ENV FLASK_RUN_PORT 8080

RUN apk add --no-cache gcc musl-dev linux-headers && \
    pip install --no-cache-dir -r requirements.txt

COPY . /srv
WORKDIR /srv
