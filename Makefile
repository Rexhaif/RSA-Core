build:
	docker build -t rsa_app:dev .

run:
	docker rm -f rsa_app
	docker run --rm -p 8888:8888 --name rsa_app rsa_app:dev