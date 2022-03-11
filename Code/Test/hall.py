import RPi.GPIO as GPIO
import time

#Initialization
GPIO.setmode(GPIO.BCM)
HALL_SENSOR= 7 #Penser à le changer
GPIO.setup(HALL_SENSOR, GPIO.IN)

hallActive = False #etat par def
etat_precedent = True
while True:
    # le senseur effet hall est HIGH aimant
    # et LOW si pas aimant
    aimant =GPIO.input(HALL_SENSOR)
    #si on détecte un aimant
    if(aimant):
       hallActive = True
       #on affiche true
       print(hallActive)
    else :
        #si pas d'aimant
        if (etat_precedent == True):
            #si aimant avant 
            hallActive = False
            #on affiche une fois le message
            print(hallActive)
    etat_precedent=aimant
       

       
        