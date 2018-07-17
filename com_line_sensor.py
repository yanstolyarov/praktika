#!/usr/bin/python
import RPi.GPIO as GPIO
import time

channel_1 = 25

GPIO.setmode(GPIO.BCM)
GPIO.setup(channel_1, GPIO.IN)

GPIO.add_event_detect(channel_1, GPIO.RISING)

while True:
    if GPIO.event_detected(channel_1):
        print('bzz')
