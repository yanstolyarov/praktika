import time
import serial

ser = serial.Serial(

    port='/dev/ttyAMA0',
    baudrate = 9600,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
    timeout=1
    )
counter=0

ser = serial.Serial(

    port='/dev/ttyUSB1',
    baudrate = 9600,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
    timeout=1
    )

while 1:
    ser.write('Write counter: %d \n'%(counter))
    x=ser.read(5)
    x=x.replace('R','1')
    y =int(x)
    c=y-1008
    print c*2.5+25
    counter += 1
