from gpiozero import LED
import time

light = LED(13)

while 1:
    light.on()
    time.sleep(1)
    light.off()
    time.sleep(1)
