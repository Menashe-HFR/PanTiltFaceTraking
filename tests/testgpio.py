import pigpio
from time import sleep

# connect to the
pi = pigpio.pi()
pan = 27
# loop forever
while True:

    pi.set_servo_pulsewidth(pan, 0)    # off
    sleep(1)
    pi.set_servo_pulsewidth(pan, 1500) # position anti-clockwise
    sleep(1)
