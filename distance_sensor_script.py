#!/usr/bin/python
from gpiozero import DistanceSensor
from time import sleep

sensor1 = DistanceSensor(23, 24)
#sensor2 = DistanceSensor(23, 24)

#while True:
#    print('Distance to nearest object is', sensor.distance, 'm')
#    sleep(0.2)

def dist_func():
    global dist1
    #global dist2
    dist1 = sensor1.distance
    #dist2 = sensor2.distance
