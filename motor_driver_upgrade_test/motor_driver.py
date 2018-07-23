from RPi import GPIO
import time


e1 = 4#left
m1 = 18
ena = 13

e2 = 6#right
m2 = 12
enb = 19

GPIO.setwarnings(False)

GPIO.setmode (GPIO.BCM)

GPIO.setup(e1,GPIO.OUT)
GPIO.setup(e2,GPIO.OUT)
GPIO.setup(m1,GPIO.OUT)
GPIO.setup(m2,GPIO.OUT)
GPIO.setup(ena,GPIO.OUT)
GPIO.setup(enb,GPIO.OUT)

p_w1 = GPIO.PWM(ena,100)#To create a PWM instance: p = GPIO.PWM(channel, frequency)
p_w2 = GPIO.PWM(enb,100)

p_w1.start(0)
p_w2.start(0)

def motor_1(x):
    p_w1.ChangeDutyCycle(x)
    if x >= 0:
        GPIO.output(m1, GPIO.LOW)
        GPIO.output(e1, GPIO.HIGH)
    else:
        GPIO.output(m1, GPIO.HIGH)
        GPIO.output(e1, GPIO.LOW)

def motor_2(x):
    p_w2.ChangeDutyCycle(x)
    if x >= 0:
        GPIO.output(m2, GPIO.LOW)
        GPIO.output(e2, GPIO.HIGH)
    else:
        GPIO.output(m2, GPIO.HIGH)
        GPIO.output(e2, GPIO.LOW)

def all_motor(x):
    p_w1.ChangeDutyCycle(x)
    p_w2.ChangeDutyCycle(x)
    if x >= 0:
        GPIO.output(m1, GPIO.LOW)
        GPIO.output(e1, GPIO.HIGH)
        GPIO.output(m2, GPIO.LOW)
        GPIO.output(e2, GPIO.HIGH)
    else:
        GPIO.output(m1, GPIO.HIGH)
        GPIO.output(e1, GPIO.LOW)
        GPIO.output(m2, GPIO.HIGH)
        GPIO.output(e2, GPIO.LOW)

def stop():
    p_w1.ChangeDutyCycle(0)
    p_w2.ChangeDutyCycle(0)
    GPIO.output(m1, GPIO.LOW)
    GPIO.output(e1, GPIO.HIGH)
    GPIO.output(m2, GPIO.LOW)
    GPIO.output(e2, GPIO.HIGH)
