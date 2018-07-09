#!/usr/bin/python
import RPi.GPIO as IO          #calling header file which helps us use GPIO’s of PI

import time                            #calling time to provide delays in program

e1 = 19                         #управляющий ШИМ-порт первого двигателя (GPIO19 например)
m1 = 12                         #управляющий порт первого двигателя
e2 = 13                         #управляющий ШИМ-порт первого двигателя
m2 = 16                         #управляющий порт первого двигателя

IO.setwarnings(False)           #do not show any warnings

IO.setmode (IO.BCM)         #we are programming the GPIO by BCM pin numbers. (PIN35 as ‘GPIO19’)

IO.setup(e1,IO.OUT)           # initialize GPIO19 as an output.
IO.setup(e2,IO.OUT)

p_w1 = IO.PWM(e1,100)          #GPIO19 as PWM output, with 100Hz frequency
p_w2 = IO.PWM(e2,100)
p_w1.start(0)                              #generate PWM signal with 0% duty cycle
p_w2.start(0)

def motor_pwm_forw_1(x):
    p_w1.ChangeDutyCycle(x)
    IO.output(m1, GPIO.LOW)

def motor_pwm_forw_2(x):
    p_w2.ChangeDutyCycle(x)
    IO.output(m2, GPIO.LOW)

def motor_pwm_reverse_1(x):
    p_w1.ChangeDutyCycle(x)
    IO.output(m1, GPIO.HIGH)

def motor_pwm_reverse_2(x):
    p_w2.ChangeDutyCycle(x)
    IO.output(m2, GPIO.HIGH)

def all_motor_pwm_forward(x):
    p_w1.ChangeDutyCycle(x)
    IO.output(m1, GPIO.LOW)
    p_w2.ChangeDutyCycle(x)
    IO.output(m2, GPIO.LOW)

def all_motor_pwm_reverse(x):
    p_w1.ChangeDutyCycle(x)
    IO.output(m1, GPIO.HIGH)
    p_w2.ChangeDutyCycle(x)
    IO.output(m2, GPIO.HIGH)

for t in range(10):
    motor_pwm_forw_1(50)
    motor_pwm_forw_2(80)
    sleep(1)
    motor_pwm_reverse_1(40)
    motor_pwm_reverse_2(60)
    sleep(2)
