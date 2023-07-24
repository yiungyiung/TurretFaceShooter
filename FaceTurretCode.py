
#160up- 320down+
import cv2
import serial,time
face_cascade= cv2.CascadeClassifier(cv2.data.haarcascades +'haarcascade_frontalface_default.xml')
cap=cv2.VideoCapture(0)
ArduinoSerial=serial.Serial('com3',115200,timeout=0.1)
time.sleep(1)
xpos=0
ypos=0
ArduinoSerial.write("m".encode('utf-8'))
while cap.isOpened():
    ret, img= cap.read()
    img=cv2.flip(img,1)  #mirror the image
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces= face_cascade.detectMultiScale(gray,1.1,6)  #detect the face
    cv2.line(img,(0,160),(640,160),(255,255,255),2)
    cv2.line(img,(0,320),(640,320),(255,255,255),2)
    cv2.line(img,(213,0),(213,480),(255,255,255),2)
    cv2.line(img,(426,0),(426,480),(255,255,255),2)
    for x,y,w,h in faces:
        xpos=x+w//2
        ypos=y+h//2
        #print(ypos,xpos)
        cv2.line(img,(xpos,0),(xpos,480),(0,255,0),2)
        cv2.line(img,(0,ypos),(640,ypos),(0,255,0),2)
        
        if(xpos>215 and xpos<430 and ypos<320 and ypos>160):
        #shoot
            ArduinoSerial.write("c".encode('utf-8'))
            #print('c')

        elif(xpos<215 and ypos<320 and ypos>160):

            ArduinoSerial.write("l".encode('utf-8'))#left
            #print('l')
        elif(xpos>430 and ypos<320 and ypos>160):
       
            ArduinoSerial.write("r".encode('utf-8'))#right
            #print('r')
        elif(ypos>320 and xpos>215 and xpos<430):#down
            ArduinoSerial.write("s".encode('utf-8'))
           # print('s')
        elif(ypos<160 and xpos>215 and xpos<430):#up
            ArduinoSerial.write("w".encode('utf-8'))
           # print('w')
        elif(xpos>430 and ypos<160 ):#top right
            ArduinoSerial.write("p".encode('utf-8'))
            #print('p')
        elif(xpos<215 and ypos<160 ):#top left
            ArduinoSerial.write("i".encode('utf-8'))
            #print('i')
        elif(xpos>430 and ypos>320 ):#bottom right
            ArduinoSerial.write("j".encode('utf-8'))
           # print('j')
        elif(xpos<215 and ypos>320 ):#bottom left
            ArduinoSerial.write("k".encode('utf-8'))
           # print('k')
        
        
        break
        
    cv2.imshow('img',img)

    if cv2.waitKey(10)&0xFF== ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
