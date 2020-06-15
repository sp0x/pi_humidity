#!/usr/bin/python
import sys
import os
import Adafruit_DHT
from slack_helper import SlackHelper
import logging
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)


led_pin = 18
dht_pin = 4
dht_type = 11
slacker = SlackHelper(os.environ['SLACK_TOKEN'])
humidity_treshold = 80
temperature_threshold = 22
slack_channel = "#team"
GPIO.setup(led_pin, GPIO.OUT)

current_readings = {
    'humidity': 0,
    'temperature': 0,
}

while True:
    humidity, temperature = Adafruit_DHT.read_retry(dht_type, dht_pin)
    last_h = current_readings['humidity']
    last_t = current_readings['temperature']
    is_alerted = False
    if last_h != humidity and humidity >= humidity_treshold:
        slacker.send(slack_channel, f'Humidity has reached a high level: {humidity}')
        is_alerted = True
    if last_t != temperature and temperature >= temperature_threshold:
        slacker.send(slack_channel, f'Temperature has reached a high degree: {temperature}')
        is_alerted = True

    GPIO.output(led_pin, GPIO.HIGH if is_alerted else GPIO.low)

    current_readings["temperature"] = temperature
    current_readings["humidity"] = humidity
    logging.info(f'Temperature: {temperature}\tHumidity: {humidity}')
