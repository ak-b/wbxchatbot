# -*- coding: utf-8 -*-

"""Main module."""
import logging

from wibot.endpoint import SparkEndpoint
from wibot.handler import MessageHandler

logging.getLogger('wibot.endpoint').addHandler(logging.StreamHandler())
logging.getLogger('wibot.endpoint').setLevel(logging.DEBUG)

logging.getLogger('wibot.handler').addHandler(logging.StreamHandler())
logging.getLogger('wibot.handler').setLevel(logging.DEBUG)

if __name__ == "__main__":
    spark_endpoint = SparkEndpoint()
    spark_endpoint.setup()

    message_handler = MessageHandler(spark_endpoint.get_websocket_url())
    message_handler.run_forever()
