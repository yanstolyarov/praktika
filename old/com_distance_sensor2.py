#!/usr/bin/env python
import time
import serial
          
ser = serial.Serial(
    port='/dev/ttyUSB1',
    baudrate = 9600,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
    timeout=1
    )
counter=0          
while 1:
    x=ser.read(5)
    x=x.replace('R','1')
    y=int(x)
    c=y-1006
    print c*2.5+20
   
