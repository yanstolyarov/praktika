#!/usr/bin/env python
import os
import time
import select
import sys
import tty
import termios
import atexit
import motor_driver_new as MD

old_settings = None
def init_anykey():
  global old_settings
  old_settings = termios.tcgetattr(sys.stdin)
  new_settings = termios.tcgetattr(sys.stdin)
  new_settings[3] = new_settings[3] & ~(termios.ECHO | termios.ICANON)
  new_settings[6][termios.VMIN] = 0
  new_settings[6][termios.VTIME] = 0
  termios.tcsetattr(sys.stdin, termios.TCSADRAIN, new_settings)

@atexit.register
def term_anykey():
  global old_settings
  if old_settings:
    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, old_settings)

def anykey():
  ch_set = []
  #ch = os.read(sys.stdin.fileno(), 1)
  ch_raw = 0
  #while ch != None and len(ch) > 0:
  #  ch_raw = sys.stdin.read(1)
  #  ch_set.append(ord(ch[0]))
  #  ch = os.read(sys.stdin.fileno(), 1)
  ch_raw = sys.stdin.read(1)
  return ch_raw

init_anykey()
counter = 0
while True:
  print 'Operation: ', counter
  counter = counter + 1
  key = anykey()
  
  if key == chr(119):
    print 'forward!'
    MD.all_motor_pwm_forward(20)
  
  time.sleep(0.2)
  
  if key == chr(115):
    print ('reverse')
    MD.all_motor_pwm_reverse(20)
  
  if key == chr(100):
    print ('right')
    MD.motor_pwm_forw_1(20)
    MD.motor_pwm_reverse_2(20)
  if key == chr(97):
    print ('left')
    MD.motor_pwm_forw_2(20)
    MD.motor_pwm_reverse_1(20)
  if key == chr(32):
    print ('stop')
    MD.stop()

