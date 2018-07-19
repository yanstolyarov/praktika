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


def button1_status():
    global curr1
    global prev1
    curr1 = GPIO.input(17)
    print("b1",curr1)
    if ((prev1 == 0) and curr1 == 0):
        print("Button1 pressed")
        a = 1
        return a
    else:
        a = 0
        return a
    prev1 = curr1

def button2_status():
    global curr2
    global prev2
    curr2 = GPIO.input(10)
    print("b2",curr2)
    if ((prev2 == 0) and curr2 == 0):
        print("Button2 pressed")
        a = 1
        return a
    else:
        a = 0
        return a
    prev2 = curr2

while 1:
    #print('button1', button1_status())
    #print('button2', button2_status())
    button1_status()
    button2_status()
