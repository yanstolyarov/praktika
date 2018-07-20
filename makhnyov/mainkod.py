import motor_driver_new as MD
import time
import com_distance_sensor1 as DS1
import com_distance_sensor2 as DS2

while 1:
    MD.all_motor_pwm_forward(50)

    dalnomer1 = DS1.dm1()
    dalnomer2 = DS2.dm2()

    if dalnomer1 < 25:
        if dalnomer2 > 25:
            time.sleep(3)
            stop()
        MD.motor_pwm_forw_1(50)
        MD.motor_pwm_reverse_2(0)

        elif dalnomer2 < 25
            time.sleep(3)
            stop()
        MD.motor_pwm_forw_2(50)
        MD.motor_pwm_reverse_1(0)
    else
        if dalnomer2 > 25:
            time.sleep(3)
            stop()
        MD.motor_pwm_forw_1(50)
        MD.motor_pwm_reverse_2(0)
