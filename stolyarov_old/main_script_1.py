from time import sleep
import motor_driver_new as MD
import com_distance_sensor_2 as DS
import button_script as BS

#side = right
t_a = 0.2 #time of moving forward/backward to make 1 step
t_b = 0.3 #time for turn on 90 degrees
p_s = 90 #power for steps
p_t = 60 #power for turns
c_a = 25 #dalnomer critical value

while 1:
    but_f1 = BS.button1_status()
    dm_2 = DS.dm2()
    if but_f == 0 and dm_2 <= c_a:
        MD.all_motor_pwm_forward(p_s)
        sleep(t_a)
        MD.stop()
    if but_f == 0 and dm_2 > c_a:
        MD.all_motor_pwm_forward(p_s)
        sleep(t_a)
        MD.stop()
        MD.motor_pwm_forw_1(p_t)
        MD.motor_pwm_reverse_2(p_t)
        sleep(t_b)
        MD.stop()
        MD.all_motor_pwm_forward(p_s)
        sleep(t_a)
        MD.stop()
    if but_f == 1 and dm_2 <= c_a:
        MD.all_motor_pwm_reverse(p_s)
        sleep(t_a)
        MD.stop()
        MD.motor_pwm_forw_2(p_t)
        MD.motor_pwm_reverse_1(p_t)
        sleep(t_b)
        MD.stop()
        MD.all_motor_pwm_forward(p_s)
        sleep(t_a)
        MD.stop()
