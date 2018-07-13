from RPi import GPIO
from gpiozero import DistanceSensor
import time
from gpiozero import Button
from signal import pause

turn = 2#turn time

e1 = 4#left
m1 = 18
e2 = 6#right
m2 = 12

GPIO.setwarnings(False)

GPIO.setmode (GPIO.BCM)

GPIO.setup(e1,GPIO.OUT)
GPIO.setup(e2,GPIO.OUT)
GPIO.setup(m1,GPIO.OUT)
GPIO.setup(m2,GPIO.OUT)
GPIO.setup(2,GPIO.OUT)
GPIO.setup(3,GPIO.OUT)

p_w1 = GPIO.PWM(e1,100)
p_w2 = GPIO.PWM(e2,100)
p_w1.start(0)
p_w2.start(0)

enab1 = GPIO.output(2, GPIO.HIGH)
enab2 = GPIO.output(3, GPIO.HIGH)

import sys,tty,termios
class _Getch:
    def __call__(self):
            fd = sys.stdin.fileno()
            old_settings = termios.tcgetattr(fd)
            try:
                tty.setraw(sys.stdin.fileno())
                ch = sys.stdin.read(3)
            finally:
                termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
            return ch

def motor_pwm_forw_1(x):
    print('right')
    p_w1.ChangeDutyCycle(x)
    GPIO.output(m1, GPIO.LOW)

def motor_pwm_forw_2(x):
    print('left')
    p_w2.ChangeDutyCycle(x)
    GPIO.output(m2, GPIO.LOW)

def motor_pwm_reverse_1(x):
    p_w1.ChangeDutyCycle(x)
    GPIO.output(m1, GPIO.HIGH)

def motor_pwm_reverse_2(x):
    p_w2.ChangeDutyCycle(x)
    GPIO.output(m2, GPIO.HIGH)

def all_motor_pwm_forward(x):
    print('forw')
    p_w1.ChangeDutyCycle(x)
    GPIO.output(m1, GPIO.LOW)
    p_w2.ChangeDutyCycle(x)
    GPIO.output(m2, GPIO.LOW)

def all_motor_pwm_reverse(x):
    print('reverse')
    p_w1.ChangeDutyCycle(x)
    GPIO.output(m1, GPIO.HIGH)
    p_w2.ChangeDutyCycle(x)
    GPIO.output(m2, GPIO.HIGH)

def get():
        inkey = _Getch()
        while(1):
                k=inkey()
                if k!='':break
        if k=='\x1b[A':
                print "up"
                all_motor_pwm_forward(80)
        elif k=='\x1b[B':
                print "down"
                all_motor_pwm_reverse(60)
        elif k=='\x1b[C':
                print "right"
                motor_pwm_forw_1(60)
        elif k=='\x1b[D':
                print "left"
                motor_pwm_forw_2(60)
        else:
                print "not an arrow key!"
                all_motor_pwm_reverse(0)

def main():
        while 1:
        #for i in range(0,20):
                get()

if __name__=='__main__':
        main()
