/* Sweep
 by BARRAGAN <http://barraganstudio.com> 
 This example code is in the public domain.

 modified 8 Nov 2013
 by Scott Fitzgerald
 http://arduino.cc/en/Tutorial/Sweep
*/ 

#include <Servo.h> 
 
Servo upleft;  // create servo object to control a servo 
int up=10;
int left=45;// twelve servo objects can be created on most boards
 int releaseupleft=30;
 Servo downright;  
 int down=10;
 int right=80;
 int releasedownright=30;
 
  Servo ab;  
 int a=30;
 int b=0;
 int releaseab=15;
 
const int analogInPin = A0; 
 int sensorValue = 0; 
int pos = 30;    // variable to store the servo position 
int serialin =0;
 
void setup() 
{ 
  upleft.attach(9);  // attaches the servo on pin 9 to the servo object 
    downright.attach(10);
    ab.attach(11);
    Serial.begin(9600);
} 
 
void loop() 
{ 
  sensorValue = analogRead(analogInPin); 
     upleft.write(releaseupleft);                              // in steps of 1 degree 
    downright.write(releasedownright);
     ab.write(pos);  
     
     
      Serial.print("sensor = " );                       
  Serial.print(sensorValue);   
  
  
    // tell servo to go to position in variable 'pos' 
    delay(20);                       // waits 15ms for the servo to reach the position 
     Serial.println(pos,'\n');
        while (Serial.available() > 0) {
              
                                                 
                 serialin= Serial.parseInt();
                 pos=serialin;
  
              
        }
} 
