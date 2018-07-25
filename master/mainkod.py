MD.stop()import motor_driver_new as MD #Импортируем код с моторов
from time import sleep #Импортируем sleep
import serial1 as S
#импорт кода дальномеров
while 1

    MD.all_motor_pwm_forward(30)
    time.sleep(0.25)
    dalnomer1 = S.dm_1()
    dalnomer2 = S.dm_2()
    print('dalnomer1', dalnomer1)
    print('dalnomer2', dalnomer2)

    if dalnomer1 < 10:
      MD.stop(1)
      if dalnomer2 > 20:
         MD.motor_pwm_forw_2(50)
         MD.motor_pwm_reverse_1(50)
         time.sleep(0.33)
         stop()
         dalnomer1 = S.dm_1()
         dalnomer2 = S.dm_2()
         print('dalnomer1', dalnomer1)
         print('dalnomer2', dalnomer2)
        if dalnomer1 > 20:
          MD.all_motor_pwm_forward(30)
          dalnomer1 = S.dm_1()
          if dalnomer1 < 5
            MD.stop(1)

      else:
        dalnomer2 < 20
        MD.motor_pwm_forw_1(50)
        MD.motor_pwm_reverse_2(50)
        time.sleep(0.4)
        MD.stop()
        dalnomer1 = S.dm_1()
        dalnomer2 = S.dm_2()
        print('dalnomer1', dalnomer1)
        print('dalnomer2', dalnomer2)

        if dalnomer1 > 20:
          MD.all_motor_pwm_forward(30)
          dalnomer1 = S.dm_1()
          if dalnomer1 < 5
            MD.stop(1)
            dalnomer1 = S.dm_1()
            dalnomer2 = S.dm_2()
            print('dalnomer1', dalnomer1)
            print('dalnomer2', dalnomer2)
        else:
          MD.motor_pwm_forw_1(50)
          MD.motor_pwm_reverse_2(50)
          time.sleep(0.4)
          MD.stop()
          MD.all_motor_pwm_forward(30)
          if dalnomer1 < 5
            MD.stop(1)
            dalnomer1 = S.dm_1()
            dalnomer2 = S.dm_2()
            print('dalnomer1', dalnomer1)
            print('dalnomer2', dalnomer2)

    else:
      dalnomer1 = S.dm_1()
      dalnomer2 = S.dm_2()
      print('dalnomer1', dalnomer1)
      print('dalnomer2', dalnomer2)

      if dalnomer2 > 20:
        MD.stop()
        MD.motor_pwm_forw_2(50)
        MD.motor_pwm_reverse_1(50)
        time.sleep(0.3)
        MD.stop()
        dalnomer1 = S.dm_1()
        dalnomer2 = S.dm_2()
        print('dalnomer1', dalnomer1)
        print('dalnomer2', dalnomer2)
        if dalnomer1 > 20:
          MD.all_motor_pwm_forward(30)
          dalnomer1 = S.dm_1()
          if dalnomer1 < 5
            MD.stop(1)
            dalnomer1 = S.dm_1()
            dalnomer2 = S.dm_2()
            print('dalnomer1', dalnomer1)
            print('dalnomer2', dalnomer2)
    if dalnomer1 < 5:
      MD.all_motor_pwm_reverse(30)
      time.sleep(1)
      MD.stop()

