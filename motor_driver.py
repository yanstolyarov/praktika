#!/usr/bin/python
#import RPi.GPIO as IO          #calling header file which helps us use GPIO’s of PI
from RPi import GPIO
import time                            #calling time to provide delays in program

e1 = 4
m1 = 18
e2 = 6
m2 = 12

GPIO.setwarnings(False)           #do not show any warnings

GPIO.setmode (GPIO.BCM)         #we are programming the GPIO by BCM pin numbers. (PIN35 as ‘GPIO19’)

GPIO.setup(e1,GPIO.OUT)           # initialize GPIO19 as an output.
GPIO.setup(e2,GPIO.OUT)
GPIO.setup(m1,GPIO.OUT)
GPIO.setup(m2,GPIO.OUT)

p_w1 = GPIO.PWM(e1,100)          #GPIO19 as PWM output, with 100Hz frequency
p_w2 = GPIO.PWM(e2,100)
p_w1.start(0)                              #generate PWM signal with 0% duty cycle
p_w2.start(0)

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

for t in range(10):
    motor_pwm_forw_1(50)
    motor_pwm_forw_2(80)
    sleep(1)
    motor_pwm_reverse_1(40)
    motor_pwm_reverse_2(60)
    sleep(2)
