import cv2
import pigpio
from time import sleep


cap = cv2.VideoCapture(0)
pi= pigpio.pi()
pan = 27  #pan- left and right
tilt = 22 #tilt- up and down
pi.set_servo_pulsewidth(pan, 1500)
pi.set_servo_pulsewidth(tilt, 2000)
in_range=200
increase= 10
currentX, currentY = 1500, 2000
w, h = 320, 240
midx, midy = w/2 , h/2


def findFace(img):
    faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(imgGray, 1.2, 8)

    cx=0
    cy=0

    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x,y), (x+w, y+h), (0,0,255), 2)
        cx = x + w // 2
        cy = y + h // 2
        #print("cx=",cx, "cy=",cy)
        #print("CX = " ,(cx*6.25+500))
        area = w * h
        #print("distans(nagtiv)=", area)
        cv2.circle(img, (cx, cy),5,(0,255,0), -1 )

    return img, cx, cy


def trackFace(targetX, currentX, targetY, currentY):
    targetX = (targetX*(2000/w)+500)
    targetY = (targetY*(2000/h)+500)
    #-----------------paning------------------------
    if targetX!=500 and abs(targetX - currentX)> in_range:
        if targetX>1500:
            currentX = currentX - (increase)
        else:
            currentX = currentX + (increase)
        print("<--------- PANING --------->")
        pi.set_servo_pulsewidth(pan,currentX)
        sleep(0.01)
    else:
        print("@@ in_range paning @@")

    #--------------tilting----------------------------

    if targetY!=500 and abs(targetY - currentY)> in_range:
        if targetY>1500:
            currentY = currentY + (increase)
        else:
            currentY = currentY - (increase)
        print(" \/ \/ \/ TILTING /\ /\ /\ ")
        pi.set_servo_pulsewidth(tilt,currentY) # position anti-clockwise
        sleep(0.01)
    else:
        print("@@ in_range tilting @@")



    return currentX, currentY


while True:
    _, img = cap.read()
    img = cv2.resize(img, (w, h))
    img, cx, cy = findFace(img)
    currentX, currentY = trackFace(cx,currentX,cy, currentY)
    cv2.imshow("cam", img)
    cv2.waitKey(2)