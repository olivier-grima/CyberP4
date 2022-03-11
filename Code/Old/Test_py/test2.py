# Import required libraries
import RPi.GPIO as GPIO

col1=25
col2=6
col3=26
col4=17
col5=27
col6=22
col7=23

def passage_jeton(channel):
    switcher = {
        25 : "colonne 1",
        6 : "colonne 2",
        26 : "colonne 3",
        17 : "colonne 4",
        27 : "colonne 5",
        22 : "colonne 6",
        23 : "colonne 7",
    }
    print(switcher.get(channel,"Colonne invalide"))

if __name__ == '__main__':
    GPIO.setmode(GPIO.BCM)
    
    GPIO.setup(col1, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(col2, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(col3, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(col4, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(col5, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(col6, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(col7, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.add_event_detect(col1, GPIO.FALLING, callback=passage_jeton, bouncetime=100)
    GPIO.add_event_detect(col2, GPIO.FALLING, callback=passage_jeton, bouncetime=100)
    GPIO.add_event_detect(col3, GPIO.FALLING, callback=passage_jeton, bouncetime=100)
    GPIO.add_event_detect(col4, GPIO.FALLING, callback=passage_jeton, bouncetime=100)
    GPIO.add_event_detect(col5, GPIO.FALLING, callback=passage_jeton, bouncetime=100)
    GPIO.add_event_detect(col6, GPIO.FALLING, callback=passage_jeton, bouncetime=100)
    GPIO.add_event_detect(col7, GPIO.FALLING, callback=passage_jeton, bouncetime=100)
    
