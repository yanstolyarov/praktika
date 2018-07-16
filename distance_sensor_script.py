#!/usr/bin/python
#from gpiozero import DistanceSensor
#from time import sleep

#sensor1 = DistanceSensor(23, 24)#echo first then trick
#sensor2 = DistanceSensor(5, 11)


#def dist1():
#    print('dist1:', sensor1.distance)

#def dist2():
#    print('dist2:', sensor2.distance)

#while True:
#    dist1()
#    dist2()




#---example---
#
from gpiozero import DistanceSensor
from time import sleep

sensor = DistanceSensor(23, 24)#echo and trigger

while True:
    print('Distance to nearest object is', sensor.distance, 'm')
    sleep(1)
