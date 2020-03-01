# Weather Service
A HTTP service to provide weather data.

# Overview
## Architecture
The service is designed with a microservices architecture.  Currently one service only is required due to the application scope, but in time more services could be added to increase functionality without changing the architecture or structure of the applcation.

Each service is located within `./services` directory. The containerised environment for each service is described in the Dockerfile.

## Technologies
* Makefile as scripts holder
* docker and docker-compose to containerise application services.
* Docker volumes to speed up local development.

## Methodologies
* Do not check in production .env file: production environment variables must be provided by the production environment

# Initialisation
* `git clone git@github.com:almccann/weather-service.git`
* `make build` to build docker images. This only needs to be run the first time or when the image must be rebuilt after changing dependencies or environment variables
* `make dev` to start the application stack
* `make clean` to stop the application stack
* `make test` to run test suite

# API
## Authentication
The API implements basic authentication:
```
user:weather
password:fintechfintech
```

## Endpoints
Request:
```
get /v1/weather?city=melbourne
```
Response:
```
{
  "wind_speed": 20,
  "temperature_degrees": 29
}
```
```
curl -u weather:fintechfintech http://localhost:8080/v1/weather?city=melbourne
```

# TODO
* handle multiple data sources
* memoisation
