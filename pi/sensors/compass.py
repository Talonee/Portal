import py_qmc5883l

class Compass:
    def __init__(self):
        self.sensor = py_qmc5883l.QMC5883L(output_range = py_qmc5883l.RNG_8G)
        self.sensor.mode_continuous()
        self.sensor.declination = 11
    
    def getDirection(self, display = True):
        data = self.sensor.get_bearing()
        if display:
            print(data)
        return data
        
    #Need to look into calibration
        
if __name__ == '__main__':
    compass = Compass()
    while True:
        
        compass.getDirection()