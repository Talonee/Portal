import serial
import pynmea2
import time
from gps_math import *

class GPS:
    serialPort = None
    coordinates = None
    ref_coordinates = None
    LST  = 0
    
    def __init__(self):
        self.port_setup()
        self.LST = time.time()
    
    def port_setup(self, port = "/dev/serial0"):
        self.serialPort = serial.Serial(port, baudrate=9600, timeout=2)

    def parseGPSdata(self):
        keywords = ["$GPRMC","$GPGGA"]
        gps_data = self.serialPort.readline()
        try:
            gps_data = gps_data.decode("utf-8")  # transform data into plain string
        except:
            return
        
        if len(gps_data) > 5:  # Check to see if the GPS gave any useful data
            if gps_data[0:6] in keywords:   # Check t see if the message code
                gps_msg = pynmea2.parse(gps_data)
                lat = gps_msg.latitude
                lng = gps_msg.longitude
                if not(lat == lng == 0):
                    self.coordinates = [lat, lng]
    
    def getXY(self, precision = 3, display = True, complete = False):
        if complete:
            self.coordinates = None
        self.parseGPSdata()
        while (self.coordinates == None and complete):
            self.parseGPSdata()
        
        if self.coordinates == None:  # if no valid data was received
            return

        coords = LanLonToCart(self.coordinates)
        location = [0,0]
        location[0] = round(coords[0], precision)
        location[1] = round(coords[1], precision)
        
        if display:
            print(f"Lat: {self.coordinates[0]}, Lon: {self.coordinates[1]}")
            print(f"X: {location[0]}, Y: {location[1]}",
                  int(1000*(time.time()-self.LST)), 'ms')
            self.LST = time.time()
        return location
    
    def setRel(self, complete = True, display = True):
        coords = self.getXY(0, False)
        while (coords == None and complete):
            coords = self.getXY(0, False)
            
        if coords == None:  
            return False
        
        self.ref_coordinates = coords
        if display:
            print(f"Origin X: {self.ref_coordinates[0]}, Y: {self.ref_coordinates[1]}")
        return True
        
    def getRelXY(self, precision = 3, display = True,complete = False):
        if self.ref_coordinates == None:
            return None
        coords = self.getXY(0, False, complete = complete)
        location = [0,0]
        location[0] = round(coords[0] -self.ref_coordinates[0], precision)
        location[1] = round(coords[1] -self.ref_coordinates[1], precision)
        
        if display:
            print(f"Lat: {self.coordinates[0]}, Lon: {self.coordinates[1]}")
            print(f"X: {location[0]}, Y: {location[1]}",
                  int(1000*(time.time()-self.LST)), 'ms')
            self.LST = time.time()
            
        return location
        
if __name__ == "__main__":
    gps = GPS()
    
    print("GPS coordinate Stream:")
    time.sleep(10)
    gps.setRel()
    while True:
        try:
            gps.getRelXY()

        except KeyboardInterrupt: #End Program
            break