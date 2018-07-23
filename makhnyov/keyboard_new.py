#!/usr/bin/python3

# adapted from https://github.com/recantha/EduKit3-RC-Keyboard/blob/master/rc_keyboard.py

import sys, termios, tty, os, time
import motor_driver_new as MD
import com_distance_sensor1 as DS1
import com_distance_sensor2 as DS2
from RPi import GPIO
#initialise a previous input variable to 0 (assume button not pressed last)
#prev_input = 0

#adjust for where your switch is connected
GPIO.setmode(GPIO.BCM)
GPIO.setup(17,GPIO.IN)
GPIO.setup(10,GPIO.IN)

sleep = 0.1
power = 20
button_delay = 0.3

#side = right
t_a = 0.2 #time of moving forward/backward to make 1 step
t_b = 0.3 #time for turn on 90 degrees
p_s = 90 #power for steps
p_t = 60 #power for turns
c_a = 25 #dalnomer critical value


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

    print('dm1: ', DS1.dm_1())
    print('dm2: ', DS2.dm_2())
    time.sleep(0.01)


    MD.all_motor_pwm_forward(50)

    dalnomer1 = DS1.dm_1()
    dalnomer2 = DS2.dm_2()

    if dalnomer1 < 25:
        if dalnomer2 > 25:
            time.sleep(3)
            MD.stop()
        MD.motor_pwm_forw_1(50)
        MD.motor_pwm_reverse_2(0)

        if dalnomer2 < 25:
            time.sleep(3)
            MD.stop()
        MD.motor_pwm_forw_2(50)
        MD.motor_pwm_reverse_1(0)
    else:
        if dalnomer2 > 25:
            time.sleep(3)
            MD.stop()
        MD.motor_pwm_forw_1(50)
        MD.motor_pwm_reverse_2(0)


    char = getch()

    if (char == "p"):
        print("Stop!")
        MD.stop()
        exit(0)

    if (char == "a"):
        print("Left pressed")
        MD.motor_pwm_forw_2(power)
        MD.motor_pwm_reverse_1(power)
        time.sleep(button_delay)
        MD.stop()

    if (char == "d"):
        print("Right pressed")
        MD.motor_pwm_forw_1(power)
        MD.motor_pwm_reverse_2(power)
        time.sleep(button_delay)
        MD.stop()

    if (char == "w"):
        print("Up pressed")
        MD.all_motor_pwm_forward(power)
        time.sleep(button_delay)
        MD.stop()

    elif (char == "s"):
        print("Down pressed")
        MD.all_motor_pwm_reverse(power)
        time.sleep(button_delay)
        MD.stop()

    if (char == "1"):
        print("Number 1 pressed")
        time.sleep(button_delay)
    if (char == " "):
        print('spacebar')
    else:
        print(char)
