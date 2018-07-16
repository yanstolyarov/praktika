#!/usr/bin/python
from gpiozero import DistanceSensor
from time import sleep

sensor1 = DistanceSensor(16, 20)#echo first then trick
sensor2 = DistanceSensor(22, 27)


def dist_func():
    global dist1
    global dist2
    dist1 = sensor1.distance
    dist2 = sensor2.distance
