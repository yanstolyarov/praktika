#!/usr/bin/python
import RPi.GPIO as GPIO
import time

channel_1 = 25

GPIO.setmode(GPIO.BCM)
GPIO.setup(channel_1, GPIO.IN)

NUM_CYCLES = 10
while True:
    start = time.time()
    for impulse_count in range(NUM_CYCLES):
        GPIO.wait_for_edge(channel_1, GPIO.FALLING)
    duration = time.time() - start      #seconds to run for loop
    frequency = NUM_CYCLES / duration   #in Hz
    print('freq:', frequency)
