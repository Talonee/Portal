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
  int rateFwd = 75;
  int rateTrn = 150;
  
  if (Serial.available() > 0) {
    int mv = Serial.read() - '0';

    // TLDR -  0123 
    switch (mv) {
      case 0:
        //Move forward
        motorRun(rateFwd, rateFwd);
        break;
      case 1:
        //Turn left
        motorRun(-rateTrn, rateTrn);
        break;
      case 2:
        //Move back
        motorRun(-rateFwd, -rateFwd);
        break;
      case 3:
        //Turn right
        motorRun(rateTrn, -rateTrn);
        break;
      case 4:
        //Stop
        motorRun(0, 0);
        break;
      default:
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
