/**********************************************************************
  Product     : Freenove 4WD Car for UNO
  Auther      : www.freenove.com
  Modification: 2019/08/03
**********************************************************************/
#define MOTOR_DIRECTION     0 //If the direction is reversed, change 0 to 1
#define PIN_DIRECTION_RIGHT 3
#define PIN_DIRECTION_LEFT  4
#define PIN_MOTOR_PWM_RIGHT 5
#define PIN_MOTOR_PWM_LEFT  6

void setup() {
  Serial.begin(9600);
  pinMode(PIN_DIRECTION_LEFT, OUTPUT);
  pinMode(PIN_MOTOR_PWM_LEFT, OUTPUT);
  pinMode(PIN_DIRECTION_RIGHT, OUTPUT);
  pinMode(PIN_MOTOR_PWM_RIGHT, OUTPUT);
}

void loop() {
  int rate = 75;
  
  if (Serial.available() > 0) {
    int mv = Serial.read() - '0';

    // TDLR -  0123 
    switch (mv) {
      case 0:
        //Move forward
        motorRun(rate, rate);
        Serial.print("up\n");
        break;
      case 1:
        //Move back
        motorRun(-rate, -rate);
        Serial.print("down\n");
        break;
      case 2:
        //Turn left
        motorRun(-rate, rate);
        Serial.print("left\n");
        break;
      case 3:
        //Turn right
        motorRun(rate, -rate);
        Serial.print("right\n");
        break;
      case 4:
        //Stop
        motorRun(0, 0);        
        Serial.print("stop\n");
        break;
      default:
        //Stop
//        motorRun(0, 0);
        break;
    }
  }
}

void motorRun(int speedl, int speedr) {
  int dirL = 0, dirR = 0;
  if (speedl > 0) {
    dirL = 0 ^ MOTOR_DIRECTION;
  } else {
    dirL = 1 ^ MOTOR_DIRECTION;
    speedl = -speedl;
  }

  if (speedr > 0) {
    dirR = 1 ^ MOTOR_DIRECTION;
  } else {
    dirR = 0 ^ MOTOR_DIRECTION;
    speedr = -speedr;
  }
  digitalWrite(PIN_DIRECTION_LEFT, dirL);
  digitalWrite(PIN_DIRECTION_RIGHT, dirR);
  analogWrite(PIN_MOTOR_PWM_LEFT, speedl);
  analogWrite(PIN_MOTOR_PWM_RIGHT, speedr);
}
