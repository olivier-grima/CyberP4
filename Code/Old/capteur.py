import RPi.GPIO as GPIO
import time


#Initialization
GPIO.setmode(GPIO.BCM)
PIR = 7
GPIO.setup(PIR, GPIO.IN)

etat_precedent = 1

print ("Ready")
while True:
    mouvement = GPIO.input(PIR)
    #renvoie 0 quand lumière refléchie ==> jeton passe
    if not mouvement:
        print("Passage d'un jeton!")
    else :
        if etat_precedent == 0:
            #renvoie 1 quand pas de retour de la lumière ==> pas de jeton
            print("Rien ")
    etat_precedent = mouvement
