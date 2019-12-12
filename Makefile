.PHONY: build-prod
build-prod:
		sudo docker build -t django-prod -f docker/Dockerfile .


.PHONY: local-start
local-start: 
		gunicorn backend.wsgi:application --bind :8000 --pythonpath backend                                         

.PHONY: dev
dev: build-dev run-dev

.PHONY: build-dev
build-dev:
		sudo docker build -t django-dev -f docker/Dockerfile .

.PHONY: run-dev
run-dev:
		sudo docker run --name django-dev -p 8000:80 django-dev &

.PHONY: stop-dev
stop-dev:
		sudo docker stop django-dev
		sudo docker rm django-dev
