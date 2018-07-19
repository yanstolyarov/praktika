#!/usr/bin/env python
import time
import serial

ser = serial.Serial(
    port='/dev/dm1_front',
    baudrate = 9600,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
    timeout=1
    )
counter=0
#while 1:
#    x=ser.read(5)
#    x=x.replace('R','1')
#    y=int(x)
#    c=y-1006
#    print c*2.5+20

def dm_1():
    ser.write('Write counter: %d \n'%(counter))
    x=ser.read(5)
    x=x.replace('R','1')
    y =int(x)
    c=y-1008
    d = c*2.5+25
    counter += 1
    return d

while 1:
    print(dm_1())
