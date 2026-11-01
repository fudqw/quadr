/*
  Analog input, analog output, serial output

 Reads an analog input pin, maps the result to a range from 0 to 255
 and uses the result to set the pulsewidth modulation (PWM) of an output pin.
 Also prints the results to the serial monitor.

 The circuit:
 * potentiometer connected to analog pin 0.
   Center pin of the potentiometer goes to the analog pin.
   side pins of the potentiometer go to +5V and ground
 * LED connected from digital pin 9 to ground

 created 29 Dec. 2008
 modified 9 Apr 2012
 by Tom Igoe

 This example code is in the public domain.

 */

// These constants won't change.  They're used to give names
// to the pins used:
 
const int analogOutPin2 = 7; // Analog output pin that the LED is attached to
const int analogOutPin3 = 8;
const int analogOutPin4 = 9;
const int analogOutPin5 = 10;
const int analogOutPinSig = 2;
const int enab = 12;
int voltage = 255;
int v5 = 100;
int dela= 50;

int sensorValue = 0;        // value read from the pot
int outputValue = 0;        // value output to the PWM (analog out)

void setup() {
  // initialize serial communications at 9600 bps:
  pinMode(analogOutPin2, OUTPUT);
  pinMode(analogOutPin3, OUTPUT);
  pinMode(analogOutPin4, OUTPUT);
  pinMode(analogOutPin5, OUTPUT);
  pinMode(analogOutPinSig, OUTPUT);
  pinMode(enab, OUTPUT);
  
}

void loop() {
  // read the analog in value:
 
  // map it to the range of the analog out:
 
  
  analogWrite(enab, 0);
  analogWrite(analogOutPinSig, voltage);
  analogWrite(analogOutPin2, voltage);
  analogWrite(analogOutPin3, voltage);
  analogWrite(analogOutPin4, voltage);
  analogWrite(analogOutPin5, voltage);

  
  // wait 2 milliseconds before the next loop
  // for the analog-to-digital converter to settle
  // after the last reading:
  delay(200);

  analogWrite(analogOutPin2, 0);
  analogWrite(analogOutPin3, 0);
  analogWrite(analogOutPin4, 0);
  analogWrite(analogOutPin5, 0);
  
 delay(dela);
  analogWrite(analogOutPin2, 0);
  analogWrite(analogOutPin3, 0);
  analogWrite(analogOutPin4, 0);
  analogWrite(analogOutPin5, voltage);
  
 delay(dela);
   analogWrite(analogOutPin2, 0);
  analogWrite(analogOutPin3, 0);
  analogWrite(analogOutPin4, voltage);
  analogWrite(analogOutPin5, 0);
  
 delay(dela);
   analogWrite(analogOutPin2, 0);
  analogWrite(analogOutPin3, 0);
  analogWrite(analogOutPin4, voltage);
  analogWrite(analogOutPin5, voltage);
  
 delay(dela);
   analogWrite(analogOutPin2, 0);
  analogWrite(analogOutPin3, voltage);
  analogWrite(analogOutPin4, 0);
  analogWrite(analogOutPin5, 0);
  
 delay(dela);
   analogWrite(analogOutPin2, 0);
  analogWrite(analogOutPin3, voltage);
  analogWrite(analogOutPin4, 0);
  analogWrite(analogOutPin5, voltage);
  
   delay(dela);
   analogWrite(analogOutPin2, 0);
  analogWrite(analogOutPin3, voltage);
  analogWrite(analogOutPin4, voltage);
  analogWrite(analogOutPin5, 0);
     delay(dela);
   analogWrite(analogOutPin2, 0);
  analogWrite(analogOutPin3, voltage);
  analogWrite(analogOutPin4, voltage);
  analogWrite(analogOutPin5, voltage);
     delay(dela);
   analogWrite(analogOutPin2, voltage);
  analogWrite(analogOutPin3, 0);
  analogWrite(analogOutPin4, 0);
  analogWrite(analogOutPin5, 0);
 delay(dela);
     analogWrite(analogOutPin2, voltage);
  analogWrite(analogOutPin3, 0);
  analogWrite(analogOutPin4, 0);
  analogWrite(analogOutPin5, voltage);
   delay(dela);
     analogWrite(analogOutPin2, voltage);
  analogWrite(analogOutPin3, 0);
  analogWrite(analogOutPin4, voltage);
  analogWrite(analogOutPin5, 0);
   delay(dela);
     analogWrite(analogOutPin2, voltage);
  analogWrite(analogOutPin3, 0);
  analogWrite(analogOutPin4, voltage);
  analogWrite(analogOutPin5, voltage);
      delay(dela);
     analogWrite(analogOutPin2, voltage);
  analogWrite(analogOutPin3, voltage);
  analogWrite(analogOutPin4, 0);
  analogWrite(analogOutPin5, 0);
      delay(dela);
     analogWrite(analogOutPin2, voltage);
  analogWrite(analogOutPin3, voltage);
  analogWrite(analogOutPin4, 0);
  analogWrite(analogOutPin5, voltage);
      delay(dela);
     analogWrite(analogOutPin2, voltage);
  analogWrite(analogOutPin3, voltage);
  analogWrite(analogOutPin4, voltage);
  analogWrite(analogOutPin5, 0);
      delay(dela);
     analogWrite(analogOutPin2, voltage);
  analogWrite(analogOutPin3, voltage);
  analogWrite(analogOutPin4, voltage);
  analogWrite(analogOutPin5, voltage);
  
  
 delay(50);
 


  
}
