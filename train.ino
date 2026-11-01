/*
  HG7881_Motor_Driver_Example - Arduino sketch
   
  This example shows how to drive a motor with using HG7881 (L9110) Dual
  Channel Motor Driver Module.  For simplicity, this example shows how to
  drive a single motor.  Both channels work the same way.
   
  This example is meant to illustrate how to operate the motor driver
  and is not intended to be elegant, efficient or useful.
   
  Connections:
   
    Arduino digital output D10 to motor driver input B-IA.
    Arduino digital output D11 to motor driver input B-IB.
    Motor driver VCC to operating voltage 5V.
    Motor driver GND to common ground.
    Motor driver MOTOR B screw terminals to a small motor.
     
  Related Banana Robotics items:
   
    BR010038 HG7881 (L9110) Dual Channel Motor Driver Module
    https://www.BananaRobotics.com/shop/HG7881-(L9110)-Dual-Channel-Motor-Driver-Module
 
  https://www.BananaRobotics.com
*/

int trigPin1 = 4;    //Trig - green Jumper
int echoPin1 = 3;    //Echo - yellow Jumper
long duration1, cm1;
int trigPin2 = 7;    //Trig - green Jumper
int echoPin2 = 6;    //Echo - yellow Jumper
long duration2, cm2;

 const int analogInPin1 = A0;
 const int analogInPin2 = A1; 
 int sensorValue1 = 0;  
 int sensorValue2 = 0;  
 int switcher=0; 
// wired connections
#define HG7881_B_IA 9 // D10 --> Motor B Input A --> MOTOR B +
#define HG7881_B_IB 10// D11 --> Motor B Input B --> MOTOR B -
#define HG7881_A_IA 11 // D10 --> Motor B Input A --> MOTOR B +
#define HG7881_A_IB 12 // D11 --> Motor B Input B --> MOTOR B -
 
// functional connections
#define MOTOR_B_PWM HG7881_B_IA // Motor B PWM Speed
#define MOTOR_B_DIR HG7881_B_IB // Motor B Direction
#define MOTOR_A_PWM HG7881_A_IA // Motor B PWM Speed
#define MOTOR_A_DIR HG7881_A_IB // Motor B Direction

 
// the actual values for "fast" and "slow" depend on the motor
#define PWM_SLOW 50  // arbitrary slow speed PWM duty cycle
#define PWM_FAST 200 // arbitrary fast speed PWM duty cycle
#define DIR_DELAY 500 // brief delay for abrupt motor changes
 
void setup()
{
  Serial.begin( 9600 );
  pinMode( MOTOR_B_DIR, OUTPUT );
  pinMode( MOTOR_B_PWM, OUTPUT );
  pinMode( MOTOR_A_DIR, OUTPUT );
  pinMode( MOTOR_A_PWM, OUTPUT );
  digitalWrite( MOTOR_B_DIR, LOW );
  digitalWrite( MOTOR_B_PWM, LOW );
  digitalWrite( MOTOR_A_DIR, LOW );
  digitalWrite( MOTOR_A_PWM, LOW );

  pinMode(trigPin1, OUTPUT);
  pinMode(echoPin1, INPUT);
  pinMode(trigPin2, OUTPUT);
  pinMode(echoPin2, INPUT);

}
 
void loop()
{
 do
 {
        digitalWrite(trigPin1, LOW);
        delayMicroseconds(5);
        digitalWrite(trigPin1, HIGH);
        delayMicroseconds(10);
        digitalWrite(trigPin1, LOW);
        

        pinMode(echoPin1, INPUT);
        duration1 = pulseIn(echoPin1, HIGH);
       
        // convert the time into a distance
        cm1 = (duration1/2) / 29.1;
      
      

        digitalWrite(trigPin2, LOW);
        delayMicroseconds(5);
        digitalWrite(trigPin2, HIGH);
        delayMicroseconds(10);
        digitalWrite(trigPin2, LOW);
        
        pinMode(echoPin2, INPUT);
        duration2 = pulseIn(echoPin2, HIGH);
      
        // convert the time into a distance
        cm2 = (duration2/2) / 29.1;

        Serial.print(cm1);
        Serial.print("cm");
          Serial.print(cm2);
        Serial.println();

        
        
        if ((cm1 >= 7)and(cm2 >= 7))
        {
          switcher=0;
          Serial.println( "WAIT" );
         }
        if ((cm1 < 7)and(cm2 >= 7))
        {
          switcher=1;
          Serial.println( "FORWARD" );
         }
        if ((cm1 >= 7)and(cm2 < 7))
        {
          switcher=2;
          Serial.println( "BACK" );
         }
        if ((cm1 < 7)and(cm2 < 7))
        {
          switcher=3;
          Serial.println( "CHARGE" );
         }


         switch (switcher)  
        {
          case 0:    // wait
        
              delay(1 );  
           break;
          case 1:    // f
                digitalWrite( MOTOR_B_DIR, LOW );
                digitalWrite( MOTOR_B_PWM, LOW );
                delay( DIR_DELAY );
                digitalWrite( MOTOR_B_DIR, LOW );
                digitalWrite( MOTOR_B_PWM, HIGH );
                digitalWrite( MOTOR_A_DIR, HIGH );
                digitalWrite( MOTOR_A_PWM, LOW );
                delay(1 );  
               break;
          case 2:   // b
                
                digitalWrite( MOTOR_B_DIR, LOW );
                digitalWrite( MOTOR_B_PWM, LOW);
                delay( DIR_DELAY );
                digitalWrite( MOTOR_B_DIR, HIGH );
                digitalWrite( MOTOR_B_PWM, LOW); 
                digitalWrite( MOTOR_A_DIR, HIGH );
                digitalWrite( MOTOR_A_PWM, LOW  );  
                    delay(1 );  
                break;
          case 3:    // charge
           
               digitalWrite( MOTOR_B_DIR, LOW );
               digitalWrite( MOTOR_B_PWM, LOW );
               digitalWrite( MOTOR_A_DIR, LOW  );
               digitalWrite( MOTOR_A_PWM, LOW );
               delay( DIR_DELAY );
               break;
        }
 
          delay(DIR_DELAY ); 


       
        
  } while(1);
 
  // repeat the main loop and redraw the menu...
}
/*EOF*/
