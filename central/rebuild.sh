#!/bin/sh

CONTAINER_NAME=openhome_central
IMAGE_NAME=pvorotnikov/openhome_central:latest

# Port configuration
PORT_OSGI=5555
PORT_MANAHER_HTTPS=8443
PORT_MANAGER_HTTP=8080

# stop container
docker stop $CONTAINER_NAME

docker rm $CONTAINER_NAME

# build image
docker build . -t $IMAGE_NAME

# run container
docker run \
    --name $CONTAINER_NAME \
    --net=host \
    -v /etc/localtime:/etc/localtime:ro \
    -v /etc/timezone:/etc/timezone:ro \
    -v /opt/openhab/conf:/openhab/conf \
    -v /opt/openhab/userdata:/openhab/userdata \
    -p $PORT_OSGI:5555 \
    -p $PORT_MANAHER_HTTPS:8443 \
    -p $PORT_MANAGER_HTTP:8080 \
    -d \
    --restart=always \
    $IMAGE_NAME
