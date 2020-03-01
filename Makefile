build:
	docker build --build-arg BUILD_DEV=1 --no-cache -t weather:latest -f ./services/weather/Dockerfile ./services/weather

dev:
	docker-compose up -d --no-recreate weather

test:
	docker-compose run --rm weather python /srv/test_app.py

clean:
	docker-compose down -v
