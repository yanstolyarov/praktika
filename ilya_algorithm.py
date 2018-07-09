from gpiozero import Button, DistanceSensor, Motor
import time

dalnomer = DistanceSensor(23, 24)
motor_l = Motor(forward=4, backward=14)
motor_r = Motor(forward=4, backward=14)
const_l1 = 0.05#расстояние от стены, на котором держится платформа
const_l2 = 0.1#критерий того, находится ли слева от платформы тупик
t = 0#период, в который повторное нажатие кнопки считается прибытием на финиш
turn = 2#время поворота

button = Button(2)

def forward():
    motor_r.forward()
    motor_l.forward()

def stop():
    motor_l.stop()
    motor_r.stop()

def backward():
    motor_l.backward()
    motor_r.backward()

while True:
    print(dalnomer.distance)
    current_time = time.time()
    if button.is_pressed:
        print("Button is pressed")
        press_button_time = time.time()
        if press_button_time <= t + 7:
            motor_l.stop()#выключить двигатели - финиш
            motor_r.stop()
            print("Finish")
            x = input()
        else
            time.sleep(2)
            #выключить двигатели
            stop()
        if dalnomer.distance < const_l2:
            #значит, слева тупик и нужно поворачивать направо
            t = time.time()
            #задний ход
            backward()
            sleep(2)
            #остановиться
            stop()
            #питание на левое колесо
            motor_l.forward()
            sleep(turn)
            #поворот завершен
            #питание на оба колеса
            forward()
            sleep(2)
        else:
            #нужен поворот налево
            #задний ход
            backward()
            sleep(2)
            #питание на правое колесо
            motor_r.forward()
            sleep(turn)
            #поворот завершен
            #питание на оба колеса
            forward()
            sleep(2)

    else:
        print("Button is not pressed")
        #питание на оба колеса
        forward()
        if dalnomer.distance < const_l1:
            #останавливаем правое колесо
            motor_r.stop()
            sleep(0.001)
            #запускаем правое колесо
            motor_r.forward()
        if dalnomer.distance > const_l1:
            #останавливаем левое колесо
            motor_l.stop()
            sleep(0.001)
            #запускаем левое колесо
            motor_l.forward()
