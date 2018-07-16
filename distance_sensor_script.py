#!/usr/bin/python
from gpiozero import DistanceSensor
from time import sleep

sensor1 = DistanceSensor(16, 20)#echo first then trick
sensor2 = DistanceSensor(22, 27)


def dist1():
    global dist1
    dist1 = sensor1.distance
    print('dist1:', dist1)

def dist2():
    global dist2
    dist1 = sensor2.distance
    print('dist2:', dist2)
