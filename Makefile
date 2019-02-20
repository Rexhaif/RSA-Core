IMAGE_NAME=rsa_core
CONTAINER_NAME=rsa-core

build:
	docker build -t $(IMAGE_NAME):dev .

stop:
	docker rm -f $(CONTAINER_NAME) || true

run-debug: stop
	docker run --rm -p 8888:8888 --name $(CONTAINER_NAME) $(IMAGE_NAME):dev

run-prod: stop
	docker run -rm --name $(CONTAINER_NAME) -d $(IMAGE_NAME):dev

run-prod-port: stop
	docker run -rm --name $(CONTAINER_NAME) -p 8888:8888 -d $(IMAGE_NAME):dev
