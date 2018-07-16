from gpiozero import DistanceSensor
from time import sleep

sensor = DistanceSensor(20, 16)
sensor2 = DistanceSensor(22, 27)

while True:
    print('Distance to nearest object is', sensor.distance, 'm')
    print('Distance to nearest object is', sensor2.distance, 'm')
    sleep(1)
