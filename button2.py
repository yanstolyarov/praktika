from RPi import GPIO
import time
import os
#initialise a previous input variable to 0 (assume button not pressed last)
prev_input = 0

#adjust for where your switch is connected
button1Pin = 17
button2Pin = 10
GPIO.setmode(GPIO.BCM)
GPIO.setup(button1Pin,GPIO.IN)
GPIO.setup(button2Pin,GPIO.IN)

while True:
    #assuming the script to call is long enough we can ignore bouncing
    if (GPIO.input(button1Pin)):
        #this is the script that will be called (as root)
        #os.system("python /home/pi/start.py"
        while True:
            #take a reading
            input = GPIO.input(17)
            #if the last reading was low and this one high, print
            if ((prev_input == 0) and input == 0):
                print("Button1 pressed")
                #update previous input
                break
            else
                print('Button1 is not pressed')
            prev_input = input
            #slight pause to debounce
            time.sleep(0.05)
    if (GPIO.input(button2Pin)):
    #this is the script that will be called (as root)
    #os.system("python /home/pi/start.py"
        while True:
            #take a reading
            input = GPIO.input(10)
            #if the last reading was low and this one high, print
            if ((prev_input == 0) and input == 0):
                print("Button2 pressed")
                #update previous input
                break
            else
                print('Button2 is not pressed')
            prev_input = input
            #slight pause to debounce
            time.sleep(0.05)
