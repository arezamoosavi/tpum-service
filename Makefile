docker-build:
	docker build -t centos-app .


docker-start:
	docker run -it --rm --name my-running-app centos-app

docker-clean:
	docker container prune
