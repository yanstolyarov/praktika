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
    print x
    counter += 1
