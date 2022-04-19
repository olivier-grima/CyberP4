import RPi.GPIO as GPIO
from RpiMotorLib import RpiMotorLib
import time


#define GPIO pins
direction = 15     #Direction (DIR) GPIO Pin
step = 18        #Step GPIO Pin
#EN_pin = 24      #enable pin (LOW to enable)

#Declare an instance of class pass GPIO pins numbers and the motor type
mymotortest = RpiMotorLib.A4988Nema(direction, step, (False,False,False), "DRV8825")
GPIO.setup(False, GPIO.OUT)

#############################
#   Actual motor control
#############################
def load(direction, steps):
    GPIO.output(False, GPIO.LOW)
    mymotortest.motor_go(direction,
                         "Full",
                          steps,
                         .005,
                         False,
                         .05) #1er false = monte
    
load(True, 315)
