#!/usr/bin/env python
import RPi.GPIO as GPIO

IRTrackingPin = 16

def setup():
    GPIO.setmode(GPIO.BOARD) # Set the GPIO pins as numbering
    GPIO.setup(IRTrackingPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def loop():
    while True:
        print(GPIO.input(IRTrackingPin))
        #if GPIO.input(IRTrackingPin) == GPIO.LOW:
#
#            print '14CORE | IR Tracking Test Code'
#            print '------------------------------'
#            print 'The sensor detects white color line'

#        else:

#            print '14CORE | IR Tracking Test Code'
#            print '------------------------------'
#            print 'The sensor detects black color line'

def destroy():
    GPIO.cleanup() # Release resource

if __name__ == '__main__': # The Program will start from here
    setup()
    try:
        loop()
    except KeyboardInterrupt: # When control c is pressed child program destroy() will be executed.
        destroy()
