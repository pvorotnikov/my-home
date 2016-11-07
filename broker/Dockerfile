
FROM rabbitmq:management

MAINTAINER Petar Vorotnikov (petar@vorotnikov.net)

ENV RABBITMQ_DEFAULT_USER=openhome
ENV RABBITMQ_DEFAULT_PASS=openhome

RUN rabbitmq-plugins enable --offline rabbitmq_mqtt

EXPOSE 1883
