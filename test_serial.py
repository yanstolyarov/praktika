#!/usr/bin/env python
import time
import serial

ser = serial.Serial(
    port='/dev/ttyUSB0',
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

#def test():
    #ser.write('Write counter: %d \n'%(counter))
    #x=ser.read(5)
    #x=x.replace('R','1')
    #y =int(x[1:4])
    #c=y-1008
    #d = c*2.5+25


while 1:
    x = ser.read(17)
    x=x.replace(' ','0')
    x1 = x[3:7]
    x2 = x[8:12]
    x3 = x[13:18]
    print(x)
    print(x1)
    print(x2)
    print(x3)
    time.sleep(1)
