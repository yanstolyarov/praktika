#!/usr/bin/python
import RPi.GPIO as GPIO
import time

channel_1 = 25

GPIO.setmode(GPIO.BCM)
GPIO.setup(channel_1, GPIO.IN)

while True:
    print(GPIO.input(channel))
