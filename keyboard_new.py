#!/usr/bin/python3

# adapted from https://github.com/recantha/EduKit3-RC-Keyboard/blob/master/rc_keyboard.py

import sys, termios, tty, os, time
import motor_driver_new as MD
import distance_sensor_script as DS
import button_script as BS

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

while True:
    print(DS.dist1(), DS.dist2())
    print(BS.button1_status(17), BS.button2_status(10))

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
