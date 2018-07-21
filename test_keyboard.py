#!/usr/bin/python3

# adapted from https://github.com/recantha/EduKit3-RC-Keyboard/blob/master/rc_keyboard.py

import sys, termios, tty, os, time
#initialise a previous input variable to 0 (assume button not pressed last)

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
    char = getch()
    if (char == "p"):
        print("Stop!")
        exit(0)
    elif (char == "d"):
        print("Left pressed")
    elif (char == "a"):
        print("Right pressed")
    elif (char == "s"):
        print("Up pressed")
    elif (char == "w"):
        print("Down pressed")
    elif (char == "1"):
        print("Number 1 pressed")
    elif (char == " "):
        print('spacebar')
    else:
        print(char)
