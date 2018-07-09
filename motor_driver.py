from gpiozero import Motor
from time import sleep

motor_l = Motor(forward=4, backward=14)

while True:
    motor_l.forward()
    sleep(2)
    motor_l.backward()
    sleep(2)
