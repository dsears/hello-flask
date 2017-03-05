# hello-flask
Hello World with Flask and Docker

# Building and deploying to Docker Hub

## Install docker

    curl -fsSL https://get.docker.com/ | sh

[Detailed instructions](https://docs.docker.com/engine/getstarted/step_one/)

## Clone the repo

    git clone https://github.com/dsears/hello-flask.git

## Build the docker image

```
$ cd hello-flask
$ docker build -t hello-flask .
...
Successfully built 8f92d2586ca8
```

## Tag it
