# hello-flask
Hello World with Flask and Docker

# Building and deploying to Docker Hub

## Install docker

    curl -fsSL https://get.docker.com/ | sh

[Detailed instructions](https://docs.docker.com/engine/getstarted/step_one/)

## Clone the repo

    git clone https://github.com/dsears/hello-flask.git

## Build and tag the docker image

```
cd hello-flask
docker build -t dsears/hello-flask:latest .
```

## Push it to Docker Hub

```
docker login
docker push dsears/hello-flask:latest
```
