import RPi.GPIO as GPIO
import time

#Initialization
GPIO.setmode(GPIO.BCM)
fin_de_course= 14 #Penser à le changer
GPIO.setup(fin_de_course, GPIO.IN)

while True:
    # le senseur effet hall est HIGH aimant
    # et LOW si pas aimant
    fin =GPIO.input(fin_de_course)
    #si on détecte un aimant
    if(fin):
       print("contact")
       

