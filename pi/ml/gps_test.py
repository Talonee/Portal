#!/usr/bin/env python3

import serial
import time

import serial
import pynmea2
import time, math

def port_setup(port):
    ser = serial.Serial(port, baudrate=9600, timeout=2)
    return ser

def parseGPSdata(ser):
        keywords = ["$GPRMC","$GPGGA"]
        gps_data = ser.readline()
        print(gps_data)
        
        try:
            gps_data = gps_data.decode("utf-8")  # transform data into plain string
        except:
            return None
        
        if len(gps_data) > 5:  # Check to see if the GPS gave any useful data
            if gps_data[0:6] in keywords:   # Check t see if the message code
                gps_msg = pynmea2.parse(gps_data)
                lat = gps_msg.latitude
                lng = gps_msg.longitude
                if lat == lng == 0:
                    return None
                else:
                    return (lat,lng)
            else:
                return None
        else:
            return None


if __name__ == '__main__':
    ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
    ser.reset_input_buffer()

    LST = time.time() #Last Success Time
    # access serial port
    gps_port = "/dev/ttyAMA4"
    gps_ser = port_setup(gps_port)

    reference = None
    relLoc = [0,0]

    #x = R * cos(lat) * cos(lon)

    #y = R * cos(lat) * sin(lon)

    #z = R *sin(lat)
    
    # Print out GPS cordinates
    print("GPS coordinate Stream:")



    while True:
        for mv in range(5):
           #mv = 1  # 0123 - T L D R

           # send int via Serial requires conversion to str(), then encode('utf-8')
           ser.write(str(mv).encode('utf-8'))


           try:
              gps_coords = parseGPSdata(gps_ser)
              if gps_coords:  # if no valid data was received
                 relLoc[0] = round(gps_coords[0], 5)
                 relLoc[1] = round(gps_coords[1], 5)
                 print(f"latitude: {relLoc[0]}, longitude: {relLoc[1]}",
                       int(1000*(time.time()-LST)), 'ms')
                 #print(time.time()-LST)
                 LST = time.time()

           except serial.SerialException as e:  # catch any serial communication errors
              print(f"\nERROR: {e}")
              print("... reconnecting to serial\n")
              ser = port_setup()

           except KeyboardInterrupt as e:  # Catch when user hits Ctrl-C and end program
              print("--- Program shutting down ---")
              break

        
           # buffer time
           time.sleep(1)
