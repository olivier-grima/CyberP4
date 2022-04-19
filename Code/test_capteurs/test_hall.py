# Import required libraries
import RPi.GPIO as GPIO

hall = 7
cpt = 0  
def passage_jeton(channel):
   cpt = cpt + 1
   print("detection ", cpt, " aimant")
   
      
    

if __name__ == '__main__':
    GPIO.setmode(GPIO.BCM)
   
    GPIO.setup(hall, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    GPIO.add_event_detect(hall, GPIO.FALLING, callback=passage_jeton, bouncetime=200)
   
    

