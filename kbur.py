#!/usr/bin/python
'''
Created on 23.01.2019

@author: lechu
'''

import serial
import time

ser = serial.Serial('/dev/ttyUSB0', 38400, timeout=1)

#     x = ser.read()          # read one byte
#     s = ser.read(10)        # read up to ten bytes (timeout)
#     line = ser.readline()   # read a '\n' terminated line

def command(cmd):
    print(cmd + ' -> ', end='')
    #ser.reset_input_buffer()
    ser.write((cmd + '\n').encode('utf-8'))
    #print(ser.readline().decode('utf-8'))
    print(ser.readline())


if __name__ == '__main__':
    command('hello')
    time.sleep(1)
    for i in range(3):
        command('set all 1100 on 3')
        time.sleep(1)
        command('set all 0011 on 3')
        time.sleep(1)
    pass
