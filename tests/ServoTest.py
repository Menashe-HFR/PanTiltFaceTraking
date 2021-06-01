from gpiozero import Servo, AngularServo
from time import sleep


tilt = AngularServo(22, min_angle=-90, max_angle=90 )
pan = AngularServo(27, min_angle= -180, max_angle=180 )
#pan- left and right
#tilt- up and down
cur =-90
ang=0
in_range=10
increase= 2 

while abs(cur - ang)> in_range:
    if cur>=0:
        ang += increase
        pan.angle =ang
        sleep(0.0001)
    else:
        ang -=increase
        pan.angle = ang
        sleep(0.1)