import com_distance_sensor1 as DS1
import com_distance_sensor2 as DS2
import time

while 1:
    print('dm1: ', DS1.dm_1())
    print('dm2: ', DS2.dm_2())
    time.sleep(0.2)
