import paho.mqtt.client as mqtt
import logging

class Client(object) :

    def __init__(self, connect_callback, message_callback, host='127.0.0.1', port=1883):
        super(Client, self).__init__()

        # create the client
        self._client = mqtt.Client()
        self._client.on_connect = connect_callback
        self._client.on_disconnect = self.on_disconnect
        self._client.on_message = message_callback

        logging.info('Connecting to {0}:{1}...'.format(host, port))

        # connect the client
        try :
            self._client.connect(host, port, 60)
        except Exception as e :
            logging.info('Error')        

        # loop the client
        self._client.loop_forever()

    # The callback for when the client gets disconnected from the server
    def on_disconnect(self, client, userdata, rc) :
        logging.info('Disconnected')
        
