#!/usr/bin/python
import sys
import os
import Adafruit_DHT
from slack_helper import SlackHelper
import logging

dht_pin = 4
dht_type = 11
slacker = SlackHelper(os.environ["SLACK_TOKEN"])
humidity_treshold = 80
temperature_threshold = 22

while True:
    h, t = Adafruit_DHT.read_retry(dht_type, dht_pin)
    if h >= humidity_treshold:
        slacker.send("#team", "Humidity has reached a high level: %f".format(h))
    if t >= temperature_threshold:
        slacker.send("#team", "Temperature has reached a high degree: %f".format(t))
    logging.info("Temperature: %f\tHumidity:%f" % (t, h))
