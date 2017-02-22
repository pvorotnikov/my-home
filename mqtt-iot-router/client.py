import paho.mqtt.client as mqtt
import logging
from threading import Thread
from multiprocessing import Queue

class Client(object) :

    def __init__(self, queue, callback, host='127.0.0.1', port=1883):
        super(Client, self).__init__()

        self._connected = False
        self._host = host
        self._port = port
        self._subscription_list = []
        self._callback = callback

        # create the client
        self._client = mqtt.Client()
        self._client.on_connect = self.on_connect
        self._client.on_message = self.on_message

        # connect the client
        self._client.connect(self._host, self._port, 60)

        logging.info('Connecting to {0}:{1}...'.format(host, port))

        # loop the client
        self._client.loop_start()
        while True :
            action, data = queue.get()
            if 'subscribe' == action :
                self.subscribe(data)
            if 'publish' == action :
                topic, message = data
                self.publish(topic, message)


    # The callback for when the client receives a CONNACK response from the server.
    def on_connect(self, client, userdata, flags, rc) :
        logging.info('Connected')
        self._connected = True
        for topic in self._subscription_list :
            client.subscribe(topic)

    # The callback for when the client gets disconnected from the server
    def on_disconnect(self, client, userdata, rc) :
        logging.info('Disconnected')
        self._connected = False

    # The callback for when a PUBLISH message is received from the server.
    def on_message(self, client, userdata, msg) :
        self._callback(msg)

    # Regiseter a callback to a subscription
    def subscribe(self, topic) :
        self._subscription_list.append(topic)
        if self._connected :
            self._client.subscribe(topic)

    # Publish message on a topic
    def publish(self, topic, message) :
        self._client.publish(topic, message)



class ClientInterface(object) :

    def __init__(self, callback, host='127.0.0.1', port=1883) :
        super(ClientInterface, self).__init__()
        self.clientQueue = Queue()
        self.clientThread = Thread(target=Client, args=(self.clientQueue, callback, host, port,))
        self.clientThread.start()

    def subscribe(self, topic) :
        self.clientQueue.put(('subscribe', topic))

    def publish(self, topic, message) :
        self.clientQueue.put(('publish', (topic, message)))


