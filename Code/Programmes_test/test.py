import RPi.GPIO as GPIO
import time
from time import sleep


#-----------------------------MOTEUR-------------------------
# Definition des pins
M1_En = 13#21
M1_In1 = 20
M1_In2 = 16

# Creation d'une liste des pins pour chaque moteur pour compacter la suite du code
Pins = [M1_In1, M1_In2]

# Setup
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(M1_En, GPIO.OUT)
GPIO.setup(M1_In1, GPIO.OUT)
GPIO.setup(M1_In2, GPIO.OUT)

# Voir aide dans le tuto
M1_Vitesse = GPIO.PWM(M1_En,80)
M1_Vitesse.start(100)

#-----------------------------FIN DE COURSE---------------------
fin_de_course= 25
GPIO.setup(fin_de_course, GPIO.IN)

#--------------------------------CAPTEUR----------------------------------
#Initialization
GPIO.setmode(GPIO.BCM)
HALL_SENSOR= 7 #Penser à le changer
GPIO.setup(HALL_SENSOR, GPIO.IN)

hallActive = False #etat par def
etat_precedent = False


def sens1() :
    GPIO.output(Pins[0], GPIO.HIGH)
    GPIO.output(Pins[1], GPIO.LOW)
    #print("Moteur tourne dans le sens 1.")

def sens2() :
    GPIO.output(Pins[0], GPIO.LOW)
    GPIO.output(Pins[1], GPIO.HIGH)
    print("Moteur tourne dans le sens 2.")
    
def arret() :
    GPIO.output(Pins[0], GPIO.LOW)
    GPIO.output(Pins[1], GPIO.LOW)
    print("Moteur s'arrete.")

cpt = 0
row = 4
while True :
    sens1()
    #print("debut")
    # le senseur effet hall est HIGH aimant
    # et LOW si pas aimant
    aimant = GPIO.input(HALL_SENSOR)
    fin =GPIO.input(fin_de_course)
    somme = aimant
    
    if(aimant):
        arret()
        for i in range(199):
            somme += aimant
            print("somme :", somme)
        mean = somme/200
        print("mean : ", mean)
            
        if(mean>1/2):
            cpt+=1
            
        
    if(fin):
            print("fin course")
            sens2()
            sleep(3)
    
    