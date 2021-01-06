#include <Wire.h> // Library for I2C communication
#include <LiquidCrystal_I2C.h> // Library for LCD
LiquidCrystal_I2C lcd = LiquidCrystal_I2C(0x27, 16, 2);
int counter = 0;
int mz80Pin = 9;
int sensorStatus = 0;
int hitObject = false;
//int resButton = 8;
//int resStatu = 0;
//int stopButton = 0;
void setup()
{
pinMode(mz80Pin, INPUT);
//pinMode(resButton, OUTPUT);
// Here I will add Buttons
lcd.init();
lcd.backlight();
}
void loop()
{
sensorStatus = digitalRead(mz80Pin);
//resStatu = digitalRead(resButton);

//if(resStatu ==HIGH){
  //counter = 0;
//}

if( (sensorStatus == 0) && (hitObject == false) ){
    counter++;
    hitObject = true;
    lcd.setCursor(1, 0);
    lcd.print("Maske Sayisi:");
    lcd.setCursor(6, 1);
    lcd.print(counter);
}
else if( (sensorStatus ==1) && (hitObject == true) ) {
    hitObject = false;
}
}
