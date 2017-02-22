#!/usr/bin/env python

# ###############################
# @author Petar Vorotnikov
# @description mqtt iot router
# ###############################

import os, sys, logging, argparse, json
from client import ClientInterface
from jsoncfg import load_config, node_exists

# program constants
DEFAULT_LOGGING_FORMAT = "%(message)s"
VERBOSE_LOGGING_FORMAT = "%(levelname)s: %(message)s (%(filename)s:%(lineno)d)"
PROGRAM = 'mqtt-iot-router'
VERSION = '1.0.0'

client = None
config = None

def main():

    global client, config

    # Get arguments
    parser = argparse.ArgumentParser(prog=PROGRAM, description=__doc__)
    parser.add_argument('config', metavar='CONFIG FILE', help="Configuration file")
    parser.add_argument('-v', '--version', action='version', version=VERSION)
    parser.add_argument('-x', '--verbose', action='store_true', help="Enable verbose logging")
    args = parser.parse_args()


    # Set logging level
    if args.verbose:
        logging.basicConfig(stream=sys.stdout, format=VERBOSE_LOGGING_FORMAT, level=logging.INFO)
    else:
        logging.basicConfig(stream=sys.stdout, format=DEFAULT_LOGGING_FORMAT, level=logging.DEBUG)

    # load config
    config = load_config(args.config)

    client = ClientInterface(on_message, host=config.HOST.value, port=config.PORT.value)
    client.subscribe(config.TOPIC_IN.value)

# republish message
def on_message(msg) :

    global client, config

    topic = msg.topic
    payload = msg.payload
    metric = msg.topic.split('/')[2]

    # create json string
    json_str = json.dumps({"metric":metric,"value":payload})

    # republish string
    client.publish(config.TOPIC_OUT.value, json_str)


if __name__ == '__main__':
    main()
