build:
	docker build --no-cache -t weather:latest -f ./services/weather/Dockerfile ./services/weather

dev:
	docker-compose up -d --no-recreate weather

test:
	docker-compose run --rm weather python test_app.py

clean:
	docker-compose down -v
