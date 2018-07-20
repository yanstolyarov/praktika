import motor_driver_new as MD
import button_script as BS
from time import sleep
p1= 30 #on the left engine to offset
p2=40  #on the right engine to offset
p3 = 90 #way back for both engine 
p4=70 #on the left engine to turn left
p5=90 #on the right engine to turn left
p6=50 #way ahead for both engine
p7=70 #on the left engine for turn right
p8=60 #on the left engine for turn right
while 1:
    but_1 = BS.button1_status()
    but_2 = BS.button2_status()
    if but_1==0 and but_2==0
        while but_2 != 1
            but_2 = BS.button2_status()
            MD.motor_pwm_forw_1(p1)
            MD.motor_pwm_forw_2(p2)
            sleep(1)
            MD.stop()
    if but_1==0 and but_2==1
        while but_1 != 1
            but_1 = BS.button1_status()
            MD.motor_pwm_forw_1(p6+5)
            MD.motor_pwm_forw_2(p6)
            sleep(1)
            MD.stop()
    if but_1==1 and but_2=0
        MD.motor_pwm_reverse_1(p3)
        MD.motor_pwm_reverse_2(p3)
        sleep(1)
        MD.stop()
        MD.motor_pwm_forw_1(p4)
        MD.motor_pwm_forw_2(p5)
        sleep(1)
        MD.stop()
    if but_1==1 and but_2=1
        MD.motor_pwm_reverse_1(p3)
        MD.motor_pwm_reverse_2(p3)
        sleep(1)
        MD.stop()         
        MD.motor_pwm_forw_1(p7)
        MD.motor_pwm_forw_2(p8)
        sleep(1)
        MD.stop()
        
