import serial
#CMDs
STOP    = b'0'
FORWARD = b'1'
REVERSE = b'2'
LEFT    = b'3'
RIGHT   = b'4'
BSTOP   = b'5'
BSTART  = b'6' 

class MotorController:
    def __init__(self, UART):
        self.m_ser = serial.Serial(UART, baudrate=115200, timeout=2)
        
    def sendCommand(self, cmd):
        self.m_ser.write(cmd)

if __name__ == '__main__':
    motorCTRL = MotorController("/dev/ttyAMA0")
    CMD_List = [STOP, FORWARD,REVERSE, LEFT, RIGHT, BSTOP, BSTART]
    for cmd in CMD_List:
        motorCTRL.sendCommand(cmd)