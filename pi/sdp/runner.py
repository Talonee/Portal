#!/usr/bin/env python3

import serial
import time

if __name__ == '__main__':
    ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
    ser.reset_input_buffer()

    while True:
        for mv in range(5):
        #mv = 1  # 0123 - T L D R

            # send int via Serial requires conversion to str(), then encode('utf-8')
            ser.write(str(mv).encode('utf-8'))
        
            # buffer time
            time.sleep(1)
