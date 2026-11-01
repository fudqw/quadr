#include <Stepper.h>
#include <EEPROM.h>

// Your specific motor has 48 steps per full revolution (7.5 degree step angle)
const int stepsPerRevolution = 48; 

// Initialize the stepper library on pins 9 through 12. 
// Standard four-pin sequence for full-step drive:
Stepper myStepper(stepsPerRevolution, 9, 10, 11, 12);

const int eepromAddress = 0;

void setup() {
  // Set speed. PM35S motors can safely run much faster than hobby motors.
  // 60 to 100 RPM is usually a good starting point for a curtain pull.
  myStepper.setSpeed(40);

  // Read the last saved direction from EEPROM
  byte directionState = EEPROM.read(eepromAddress);

  if (directionState > 1) {
    directionState = 0;
  }

  // 500mm / (35mm * PI) * 48 steps = ~218 steps
  long stepsToTravel = 200;

  // Alternate direction based on the saved state
  if (directionState == 0) {
    // Open/Close Counter-Clockwise
    myStepper.step(-stepsToTravel);
    EEPROM.write(eepromAddress, 1); // Save next state
  } 
  else {
    // Open/Close Clockwise
    myStepper.step(stepsToTravel);
    EEPROM.write(eepromAddress, 0); // Save next state
  }
}

void loop() {
  // Keep empty so it only triggers once per power cycle
}
