#!/usr/bin/python3

# adapted from https://github.com/recantha/EduKit3-RC-Keyboard/blob/master/rc_keyboard.py

import sys, termios, tty, os, time
import motor_driver_new as MD
from time import sleep
import com_distance_sensor_1 as DS1
import com_distance_sensor_2 as DS2
import button_script as BS

from RPi import GPIO
#initialise a previous input variable to 0 (assume button not pressed last)
prev_input = 0

#adjust for where your switch is connected
GPIO.setmode(GPIO.BCM)
GPIO.setup(17,GPIO.IN)
GPIO.setup(10,GPIO.IN)

sleep = 0.1
power = 40
button_delay = 0.3

prev1 = 1
prev2 = 1
curr1 = 1
curr2 = 2

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
    print('button1: ',BS.button1_status())
    print('button2: ',BS.button2_status())
    print('dm1: ',DS1.dm1())
    print('dm2: ',DS2.dm2())

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
