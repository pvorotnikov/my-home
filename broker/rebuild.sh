#!/bin/sh

CONTAINER_NAME=oh_broker
IMAGE_NAME=pvorotniko/oh:latest
CONTAINER_HOSTNAME=oh-broker

# stop container
docker stop $CONTAINER_NAME

docker rm $CONTAINER_NAME

# build image
docker build . -t $IMAGE_NAME

# run container
docker run -d \
	--hostname $CONTAINER_HOSTNAME \
	--name $CONTAINER_NAME \
	-p 8080:15672 \
	$IMAGE_NAME
