#!/usr/bin/python3

# adapted from https://github.com/recantha/EduKit3-RC-Keyboard/blob/master/rc_keyboard.py

import sys, termios, tty, os, time
import motor_driver_new as MD
from gpiozero import DistanceSensor
from time import sleep

from RPi import GPIO
import time
import os
#initialise a previous input variable to 0 (assume button not pressed last)
prev_input = 0

#adjust for where your switch is connected
GPIO.setmode(GPIO.BCM)
GPIO.setup(17,GPIO.IN)
GPIO.setup(10,GPIO.IN)

prev1 = 1
prev2 = 1
curr1 = 1
curr2 = 2

sensor1 = DistanceSensor(20, 16)#echo first then trick
sensor2 = DistanceSensor(22, 27)

def button1_status(pin):
    global curr1
    global prev1
    curr1 = GPIO.input(pin)
    #print("b1",curr1)
    if ((prev1 == 0) and curr1 == 0):
        print("Button1 pressed")
    prev1 = curr1

def button2_status(pin):
    global curr2
    global prev2
    curr2 = GPIO.input(pin)
    #print("b2",curr2)
    if ((prev2 == 0) and curr2 == 0):
        print("Button2 pressed")
    prev2 = curr2

def getch():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)

    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch

sleep = 0.1
power = 40
button_delay = 0.3

def dist1():
    global dist1
    dist1 = sensor1.distance
    print('dist1:', dist1)

def dist2():
    global dist2
    dist1 = sensor2.distance
    print('dist2:', dist2)

while True:
    dist1()
    dist2()
    button1_status(17)
    button2_status(10)

    char = getch()


    if (char == "p"):
        print("Stop!")
        exit(0)

    elif (char == "a"):
        print("Left pressed")
        MD.motor_pwm_forw_2(power)
        MD.motor_pwm_reverse_1(power)
        time.sleep(button_delay)
        MD.stop()

    elif (char == "d"):
        print("Right pressed")
        MD.motor_pwm_forw_1(power)
        MD.motor_pwm_reverse_2(power)
        time.sleep(button_delay)
        MD.stop()

    elif (char == "w"):
        print("Up pressed")
        MD.all_motor_pwm_forward(power)
        time.sleep(button_delay)
        MD.stop()

    elif (char == "s"):
        print("Down pressed")
        MD.all_motor_pwm_reverse(power)
        time.sleep(button_delay)
        MD.stop()

    elif (char == "1"):
        print("Number 1 pressed")
        time.sleep(button_delay)
    elif (char == " "):
        print('spacebar')
    else:
        print(char)
