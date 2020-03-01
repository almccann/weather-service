FROM python:3.7-alpine

ARG BUILD_DEV
# if --build-arg BUILD_DEV=1 set IMAGE_ENV 'dev' otherwise null
ENV IMAGE_ENV=${BUILD_DEV:+dev}
# if IMAGE_ENV is null, set it to 'prod' (or otherwise leave as is)
ENV IMAGE_ENV=${IMAGE_ENV:-prod}

COPY weather.txt requirements.txt
COPY ${IMAGE_ENV}.env .env

COPY . /srv

RUN apk add --no-cache gcc musl-dev linux-headers && \
    pip install --no-cache-dir -r requirements.txt
