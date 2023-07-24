
#include <Servo.h>
int deg=90,val=5,valy=3;
int degy=90;
String x;
Servo servo;
Servo servoy;
void setup() {
 Serial.begin(9600);
 Serial.setTimeout(1);
 servo.attach(5); //D1
 servo.write(90);
 servoy.attach(6);
 servoy.write(90);
 deg=90;
 degy=90;
}
void loop() {

 if (Serial.available()>0){
 x = Serial.readString();
 if(x=="c")
 {
   Serial.print("shoot");
 }
 else if(x=="r")
 {//right
   deg=deg+val;
   if(deg>=180){
     deg=180;
   }
   servo.write(deg);
 }
 else if(x=="l")
 {//left
   deg=deg-val;
   if(deg<=0){
     deg=0;
   }
   servo.write(deg);
 }
 else if (x=="s")
 {
   degy=degy-valy;
   if(degy<=0){
     degy=0;
   }
   servoy.write(degy);
 }
 else if (x=="w")
 {
   degy=degy+valy;
   if(degy>=180){
     degy=180;
   }
   servoy.write(degy);
 }
 else if (x=="p")
 {
   degy=degy+valy;
   deg=deg+val;
   if(degy>=180){
     degy=180;
   }
   
   
   if(deg>=180){
     deg=180;
   }
   servoy.write(degy);
   servo.write(deg);
 }
 else if (x=="i")
 {
   degy=degy+valy;
   deg=deg-val;
   if(degy>=180){
     degy=180;
   }
   
   
   if(deg<=0){
     deg=0;
   }
   servoy.write(degy);
   servo.write(deg);
 }
 else if (x=="k")
 {
   degy=degy-valy;
   deg=deg-val;
   if(degy<=0){
     degy=0;
   }
   
   
   if(deg<=0){
     deg=0;
   }
   servoy.write(degy);
   servo.write(deg);
 }
 else if (x=="j")
 {
   degy=degy-valy;
   deg=deg+val;
   if(degy<=0){
     degy=0;
   }
   
   
   if(deg>=180){
     deg=180;
   }
   servoy.write(degy);
   servo.write(deg);
 }
 else if(x=="m")
 {
   servo.write(90);
 }
 }
 }
