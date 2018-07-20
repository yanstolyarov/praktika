#!/usr/bin/python3

# adapted from https://github.com/recantha/EduKit3-RC-Keyboard/blob/master/rc_keyboard.py

import sys, termios, tty, os, time
import motor_driver_new as MD
import time
from RPi import GPIO
#initialise a previous input variable to 0 (assume button not pressed last)
#prev_input = 0

#adjust for where your switch is connected
GPIO.setmode(GPIO.BCM)
GPIO.setup(17,GPIO.IN)
GPIO.setup(10,GPIO.IN)
p1= 30 #on the left engine to offset
p2=70  #on the right engine to offset
p3 = 90 #way back for both engine
p4=50 #on the left engine to turn left
p5=90 #on the right engine to turn left
p6=50 #way ahead for both engine
p7=70 #on the left engine for turn right
p8=20 #on the left engine for turn right
button_delay = 0.3

sleep = 0.1
power = 40


def button1_status():
    curr1 = GPIO.input(17)
    #print("b1",curr1)
    if curr1 == 0:
        return 1
    else:
        return 0

def button2_status():
    curr2 = GPIO.input(10)
    #print("b2",curr2)
    if curr2 == 0:
        return 1
    else:
        return 0

but_1 = button1_status()
but_2 = button2_status()


def getch():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)

    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch


while True:
    but_1 = button1_status()
    but_2 = button2_status()
    print(but_1,but_2)
    if but_1==0 and but_2==0:
        MD.motor_pwm_forw_1(p1)
        MD.motor_pwm_forw_2(p2)
        time.sleep(1)
        MD.stop()
        print('1if')
    print('11if')
    if but_1==0 and but_2==1:
        MD.motor_pwm_forw_1(p6+30)
        MD.motor_pwm_forw_2(p6)
        time.sleep(1)
        MD.stop()
        print('2if')
    print('22if')    
    if but_1==1 and but_2==0:
        MD.motor_pwm_reverse_1(p3)
        MD.motor_pwm_reverse_2(p3)
        time.sleep(1)
        MD.stop()
        MD.motor_pwm_forw_1(p4)
        MD.motor_pwm_forw_2(p5)
        time.sleep(1)
        MD.stop()
        print('3if') 
    print('33if') 
    if but_1==1 and but_2==1:
        MD.motor_pwm_reverse_1(p3)
        MD.motor_pwm_reverse_2(p3)
        time.sleep(1)
        MD.stop()
        MD.motor_pwm_forw_1(p7)
        MD.motor_pwm_forw_2(p8)
        time.sleep(1)
        MD.stop()
        print('4if') 
    print('44if') 

    char = getch()

    if (char == "p"):
        print("Stop!")
        MD.stop()
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
    #else:
        #print(char)
