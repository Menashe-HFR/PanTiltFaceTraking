import cv2
from gpiozero import Servo, AngularServo
from time import sleep

cap = cv2.VideoCapture(0)
tilt = AngularServo(22, min_angle=-180, max_angle=180 )#tilt- up and down
pan = AngularServo(27, min_angle= -180, max_angle=180 )#pan- left and right

in_range=10
increase= 2

def findFace(img):
    faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(imgGray, 1.2, 8)

    myFaceListC = []
    myFaceListArea = []

    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x,y), (x+w, y+h), (0,0,255), 2)
        cx = x + w // 2
        cy = y + h // 2
        area = w * h
        cv2.circle(img, (cx, cy),5,(0,255,0), cv2.FILLED )
        myFaceListC.append([cx,cy])
        myFaceListArea.append(area)
    if len(myFaceListArea) != 0:
        i= myFaceListArea.index(max(myFaceListArea))
        return img, [myFaceListC[i],myFaceListArea[i]]
    else:
        return img, [[0,0],0]


while True:
    _, img = cap.read()
    findFace(img)
    cv2.imshow("cam", img)
    cv2.waitKey(1)