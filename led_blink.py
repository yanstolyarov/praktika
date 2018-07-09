from gpiozero import LED
from time import sleep

light = LED(2)

while True:
    light.on()
    sleep(1)
    light.off()
    sleep(1)
