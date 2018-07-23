import motor_driver_new as MD
import time
import com_distance_sensor1 as DS1
import com_distance_sensor2 as DS2

while 1:
    MD.all_motor_pwm_forward(50)
    time.sleep(0.25)
    dalnomer1 = DS1.dm_1()
    dalnomer2 = DS2.dm_2()
    print('dalnomer1', dalnomer1)
    print('dalnomer2', dalnomer2)

    if dalnomer1 < 20:
        MD.stop()
        time.sleep(2)
        if dalnomer2 > 25:
          MD.motor_pwm_forw_1(50)
          MD.motor_pwm_reverse_2(0)
          time.sleep(0.6)
          MD.stop()
	else:
	  MD.motor_pwm_forw_2(50)
	  MD.motor_pwm_reverse_1(0)
	  time.sleep(0.6)
	  MD.stop()
    else:
      if dalnomer2 > 25:
        MD.motor_pwm_forw_1(50)
        MD.motor_pwm_reverse_2(0)
        time.sleep(0.6)
        MD.stop()
