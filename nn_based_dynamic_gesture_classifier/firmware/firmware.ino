// include the "Wire" library.
// this is essential for i2c communication
#include <Wire.h>

// defines a constant with the i2c address of the adxl345 sensor
// the address 0x53 is the standard address when the SDO pin of the ADXL345 sensor is connected to the ground
const int ADXL345_ADDR = 0x53;

void setup() {
  // initializing the serial communication at a baud rate of 9600
  Serial.begin(9600);
  // initializing the "Wire" library
  Wire.begin();

  // initializing adxl345
  // calling writeRegister() function to write to the adxl345's POWER_CTL register (address 0x2D)
  // the value 0x08 sets the sensor to measurement mode, turning it ON
  writeRegister(0x2D, 0x08);
  // calling writeRegister() function to write data to the DATA_FORMAT register (address 0x31)
  // the value 0x08 configures the sensor for the full resoution and a measurement range of +/- 2g
  writeRegister(0x31, 0x08);
}

void loop() {
  // declaring 3 variables to store the accelerometer readings
  float x, y, z;

  // calling the readXYZ() function to read the accelerometer data and store in the declare variables (x, y, z)
  readXYZ(x, y, z);

  // printing the values
  Serial.print(x); // blue
  Serial.print(",");
  Serial.print(y); // red
  Serial.print(",");
  Serial.print(z); // green
  // using println() to end the line
  Serial.println();

  // introducing a delay before the next reading
  delay(150);
}

// defining a function that writes a byte "value" to a specific register "reg" on adxl345
void writeRegister(byte reg, byte value) {
  
  // start an i2c transmission to the adxl345 sensor
  Wire.beginTransmission(ADXL345_ADDR);
  // send the register address "reg" to the sensor
  Wire.write(reg);
  // send the data "value" to the specified register
  Wire.write(value);
  // end the i2c transmission
  Wire.endTransmission();
}

// defining a function readXYZ(), to read the x, y, z axis acceleration data from adxl345 sensor
// "&" symbol indicates that x, y, z are passed by reference
// changes to them will also affect the variables in the loop() function

void readXYZ(float &x, float &y, float &z) {

  // start an i2c transmission to adxl345
  Wire.beginTransmission(ADXL345_ADDR);
  // send the address of DATAX0 register, which is where the x-axis acceleration data starts
  Wire.write(0x32);
  // ending the transmission, but sending a repeated start condition
  // this allows the Arduino to immediately request data from the adxl345 sensor without releasing the i2c bus
  Wire.endTransmission(false);
  // requesting 6 bytes of data from the adxl345 sensor
  // this corresponds to th x, y, z axis acceleration data (2 bytes per axis)
  Wire.requestFrom(ADXL345_ADDR, 6);
  // perform a conditional check if 6 bytes of data are available from the adxl345 sensor
  if (Wire.available() == 6) {
    // reading the low byte of the x-axis acceleration data
    int16_t x_raw = Wire.read();
    // reading the high byte of x-axis data and combining it with the low byte to form a 16-bit signed integer
    x_raw |= Wire.read() << 8;
    // reading the low byte of the x-axis acceleration data
    int16_t y_raw = Wire.read();
    // reading the high byte of x-axis data and combining it with the low byte to form a 16-bit signed integer
    y_raw |= Wire.read() << 8;
    // reading the low byte of the x-axis acceleration data
    int16_t z_raw = Wire.read();
    // reading the high byte of x-axis data and combining it with the low byte to form a 16-bit signed integer
    z_raw |= Wire.read() << 8;

    // converting the raw 16-bit integer to floating point in g's
    // the division by 256.0 is due to full resolution mode and +/- 2g range
    x = (float)x_raw / 256.0;
    y = (float)y_raw / 256.0;
    z = (float)z_raw / 256.0;
  }
}
