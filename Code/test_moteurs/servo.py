import RPi.GPIO as GPIO
import time

servoPIN = 12
GPIO.setmode(GPIO.BCM)
GPIO.setup(servoPIN, GPIO.OUT)

p = GPIO.PWM(servoPIN, 50) # GPIO 17 for PWM with 50Hz
p.start(2.5) # Initialization

#1ms -> 0°
#1/20*100 = 5% : duty cycle

#1.5 ms -> 90°
#1.5/20*100 = 7.5%

#2 ms -> 180°
#2/20*100 = 10%




#
try:
  while True:
    p.ChangeDutyCycle(11)
    time.sleep(0.5)
    p.ChangeDutyCycle(5)
    time.sleep(0.5)
    

except KeyboardInterrupt:
  p.stop()
  GPIO.cleanup()