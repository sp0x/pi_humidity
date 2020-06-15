import logging
import os
from slack import WebClient
from slack.errors import SlackApiError

logging.basicConfig(level=logging.INFO)


class SlackHelper(object):

    def __init__(self, token):
        self.client = WebClient(token=token)

    def send(self, channel, message):
        try:
            self.client.chat_postMessage(channel=channel, text=message)
        except SlackApiError as e:
            assert e.response["error"]
