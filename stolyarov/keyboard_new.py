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
power = 40
button_delay = 0.3

#side = right
t_a = 0.2 #time of moving forward/backward to make 1 step
t_b = 0.3 #time for turn on 90 degrees
p_s = 50 #power for steps
p_t = 40 #power for turns
c_a = 9 #dalnomer critical value

def button1_status():
    curr1 = GPIO.input(17)
    #print("b1",curr1)
    if curr1 == 0:
        return "True"
    else:
        return "False"

def button2_status():
    curr2 = GPIO.input(10)
    #print("b2",curr2)
    if curr2 == 0:
        return "True"
    else:
        return "False"

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
    but_f = button1_status()
    dm_2 = DS2.dm_2()
    print('button1: ',button1_status())
    print('button2: ',button2_status())
    print('dm1: ', DS1.dm_1())
    print('dm2: ', DS2.dm_2())
    time.sleep(0.01)


    if but_f == "False" and DS2.dm_2() <= c_a:
        MD.all_motor_pwm_forward(p_s)
        time.sleep(t_a)
        MD.stop()

    if but_f == "False" and DS2.dm_2() > c_a:
        MD.all_motor_pwm_forward(p_s)
        time.sleep(t_a)
        MD.stop()
        MD.motor_pwm_forw_1(p_t)
        MD.motor_pwm_reverse_2(p_t)
        time.sleep(t_b)
        MD.stop()
        MD.all_motor_pwm_forward(p_s)
        time.sleep(t_a)
        MD.stop()

    if but_f == "True" and DS2.dm_2() <= c_a:
        MD.all_motor_pwm_reverse(p_s)
        time.sleep(t_a)
        MD.stop()
        MD.motor_pwm_forw_2(p_t)
        MD.motor_pwm_reverse_1(p_t)
        time.sleep(t_b)
        MD.stop()
        MD.all_motor_pwm_forward(p_s)
        time.sleep(t_a)
        MD.stop()

    if but_f == "True" and DS2.dm_2() <= c_a:
        MD.all_motor_pwm_reverse(p_s)
        time.sleep(t_a)
        MD.stop()
        MD.motor_pwm_forw_1(p_t)
        MD.motor_pwm_reverse_2(p_t)
        time.sleep(t_b)
        MD.stop()
        MD.all_motor_pwm_forward(p_s)
        time.sleep(t_a)
        MD.stop()


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
    else:
        print(char)
