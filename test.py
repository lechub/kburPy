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
    print(cmd + ' :>')
    ser.write((cmd + '\n').encode('utf-8'))
    print((cmd + '\n').encode('utf-8'))
#    ser.write('\n')
    print(ser.readline())

def test():
    #ser.reset_input_buffer()
    for x in range(0, 5): 
        cmd = 'get all on 3'
        print(cmd + '  >')
        ser.write(cmd.encode('utf-8'))
        ser.write(b'\n')
        print(ser.readline())
        time.sleep(1)
        
        #ser.reset_input_buffer()
        cmd = 'get all on 3\n'
        print(cmd + '  >')
        ser.write(cmd.encode('utf-8'))
        print(ser.readline())
        time.sleep(1)
   


if __name__ == '__main__':
    command('hello')
    command('get all on 3')
    command('set all 0101 on 3')
    command('set out 1 hi on 3')
    pass
