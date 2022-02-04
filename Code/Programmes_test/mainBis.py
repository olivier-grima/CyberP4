import RPi.GPIO as GPIO
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
pwm = GPIO.PWM(M1_En,10)
pwm.start(100)

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

while True :
    
    print("debut")
    # le senseur effet hall est HIGH aimant
    # et LOW si pas aimant
    aimant =GPIO.input(HALL_SENSOR)
    fin =GPIO.input(fin_de_course)
    if(fin):
        print("fin course")
        sens2()
        sleep(3)
    #si on détecte un aimant
    row=3
    i=0
    while(i<row-1):
        sens1()
        if(etat_precedent == True and aimant == False):
            i+=1
            print(i)
        
        print("etat prec :", etat_precedent)    
        etat_precedent=aimant
        print("etat prec :", etat_precedent)
        print("--")
    if(aimant):
        arret()
        
    if(fin):
            print("fin course")
            sens2()
            sleep(3)
    
    

    