from RPi import GPIO
import time
import os
#initialise a previous input variable to 0 (assume button not pressed last)
prev_input = 0

#adjust for where your switch is connected
buttonPin = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(buttonPin,GPIO.IN)

while True:
  #assuming the script to call is long enough we can ignore bouncing
  if (GPIO.input(buttonPin)):
    #this is the script that will be called (as root)
    #os.system("python /home/pi/start.py"
    while True:
        #take a reading
        input = GPIO.input(17)
        #if the last reading was low and this one high, print
        if ((not prev_input) and input):
        print("Button pressed")
        #update previous input
        prev_input = input
        #slight pause to debounce
        time.sleep(0.05))
    else:
        break
