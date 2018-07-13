#!/usr/bin/python

from RPi import GPIO
from gpiozero import DistanceSensor
import time
from gpiozero import Button
from signal import pause

button = Button(2)

sensor1 = DistanceSensor(23, 24)
sensor2 = DistanceSensor(27, 22)

const_l1 = 0.05#distance from the wall on which the platform rests
const_l2 = 0.1#the criterion of whether there is a dead end to the platform
turn = 2#turn time

e1 = 4#left
m1 = 18
e2 = 6#right
m2 = 12

GPIO.setwarnings(False)

GPIO.setmode (GPIO.BCM)

GPIO.setup(e1,GPIO.OUT)
GPIO.setup(e2,GPIO.OUT)
GPIO.setup(m1,GPIO.OUT)
GPIO.setup(m2,GPIO.OUT)

p_w1 = GPIO.PWM(e1,100)
p_w2 = GPIO.PWM(e2,100)
p_w1.start(0)
p_w2.start(0)

enab1 = GPIO.output(21, GPIO.HIGH)
enab2 = GPIO.output(19, GPIO.HIGH)

def motor_pwm_forw_1(x):
    p_w1.ChangeDutyCycle(x)
    GPIO.output(m1, GPIO.LOW)

def motor_pwm_forw_2(x):
    p_w2.ChangeDutyCycle(x)
    GPIO.output(m2, GPIO.LOW)

def motor_pwm_reverse_1(x):
    p_w1.ChangeDutyCycle(x)
    GPIO.output(m1, GPIO.HIGH)

def motor_pwm_reverse_2(x):
    p_w2.ChangeDutyCycle(x)
    GPIO.output(m2, GPIO.HIGH)

def all_motor_pwm_forward(x):
    p_w1.ChangeDutyCycle(x)
    GPIO.output(m1, GPIO.LOW)
    p_w2.ChangeDutyCycle(x)
    GPIO.output(m2, GPIO.LOW)

def all_motor_pwm_reverse(x):
    p_w1.ChangeDutyCycle(x)
    GPIO.output(m1, GPIO.HIGH)
    p_w2.ChangeDutyCycle(x)
    GPIO.output(m2, GPIO.HIGH)

def info():
    print('sensor1',sensor1.distance,'m')
    print('sensor2',sensor2.distance,'m')

for t in range(20):
    t += 1
    info()
    motor_pwm_forw_1(30)
    motor_pwm_reverse_2(50)
    time.sleep(2)
    info()
    all_motor_pwm_forward(90)
    time.sleep(2)
    all_motor_pwm_reverse(40)
    info()
