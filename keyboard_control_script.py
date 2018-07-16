from RPi import GPIO
from gpiozero import DistanceSensor
import time
from gpiozero import Button
from signal import pause
import sys,tty,termios

e1 = 18#left
m1 = 4
e2 = 12#right
m2 = 6
ena = 2
enb = 3

GPIO.setwarnings(False)

GPIO.setmode (GPIO.BCM)

GPIO.setup(e1,GPIO.OUT)
GPIO.setup(e2,GPIO.OUT)
GPIO.setup(m1,GPIO.OUT)
GPIO.setup(m2,GPIO.OUT)
GPIO.setup(ena,GPIO.OUT)
GPIO.setup(enb,GPIO.OUT)

GPIO.output(ena, GPIO.HIGH)
GPIO.output(enb, GPIO.HIGH)
p_w1 = GPIO.PWM(e1,100)
p_w2 = GPIO.PWM(e2,100)
p_w1.start(0)
p_w2.start(0)



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
    p_w1.ChangeDutyCycle(x)
    GPIO.output(m1, GPIO.LOW)

def motor_pwm_forw_2(x):
    p_w2.ChangeDutyCycle(x)
    GPIO.output(m2, GPIO.LOW)

def motor_pwm_reverse_1(x):
    p_w1.ChangeDutyCycle(x)
    GPIO.output(m1, GPIO.HIGH)

def motor_pwm_reverse_2(x):
    p_w2.ChangeDutyCycle(x)
    GPIO.output(m2, GPIO.HIGH)

def all_motor_pwm_forward(x):
    p_w1.ChangeDutyCycle(x)
    GPIO.output(m1, GPIO.LOW)
    p_w2.ChangeDutyCycle(x)
    GPIO.output(m2, GPIO.LOW)

def all_motor_pwm_reverse(x):
    p_w1.ChangeDutyCycle(x)
    GPIO.output(m1, GPIO.HIGH)
    p_w2.ChangeDutyCycle(x)
    GPIO.output(m2, GPIO.HIGH)

def stop():
    p_w1.ChangeDutyCycle(0)
    GPIO.output(m1, GPIO.LOW)
    p_w2.ChangeDutyCycle(0)
    GPIO.output(m2, GPIO.LOW)

def get():
        inkey = _Getch()
        while(1):
                k=inkey()
                if k!='':break
        if k=='\x1b[A':
                #print "up"
                all_motor_pwm_forward(40)
                time.sleep(0.2)
                stop()
        elif k=='\x1b[B':
                #print "down"
                all_motor_pwm_reverse(40)
                time.sleep(0.2)
                stop()
        elif k=='\x1b[C':
                #print "right"
                motor_pwm_forw_1(40)
                motor_pwm_reverse_2(40)
                time.sleep(0.2)
                stop()
        elif k=='\x1b[D':
                #print "left"
                motor_pwm_forw_2(40)
                motor_pwm_reverse_1(40)
                time.sleep(0.2)
                stop()
        else:
                #print "not an arrow key!"
                stop()
                time.sleep(0.2)


def main():
        for i in range(0,20):
                get()

if __name__=='__main__':
        main()
