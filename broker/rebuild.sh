#!/bin/sh

CONTAINER_NAME=openhome_broker
IMAGE_NAME=pvorotnikov/openhome_broker:latest
CONTAINER_HOSTNAME=openhome-broker

# Port configuration
PORT_AMQP=5672
PORT_MQTT=1883
PORT_MANAGER_HTTP=8081

# stop container
docker stop $CONTAINER_NAME

docker rm $CONTAINER_NAME

# build image
docker build . -t $IMAGE_NAME

# run container
docker run \
    --name $CONTAINER_NAME \
    --hostname $CONTAINER_HOSTNAME \
    -p $PORT_AMQP:5672 \
    -p $PORT_MQTT:1883 \
    -p $PORT_MANAGER_HTTP:15672 \
    -d \
    --restart=always \
    $IMAGE_NAME
