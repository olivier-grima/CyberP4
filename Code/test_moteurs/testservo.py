import RPi.GPIO as GPIO
import time 

GPIO.setmode(GPIO.BCM)
GPIO.setup(12, GPIO.OUT)
GPIO.setwarnings(True)

ajoutAngle = 5

angle1 = 90;
angle2 = 180;
duree = 2;
duree2 = 0.5;


angleChoisi1 = angle1/10 + ajoutAngle
angleChoisi2 = angle2/10 + ajoutAngle

pwm=GPIO.PWM(12,100)
pwm.start(5)

    
pwm.ChangeDutyCycle(angleChoisi1)
time.sleep(duree)
pwm.ChangeDutyCycle(angleChoisi2)
time.sleep(duree2)
pwm.stop()
