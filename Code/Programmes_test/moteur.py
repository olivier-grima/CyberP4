import RPi.GPIO as GPIO
from time import sleep


# Definition des pins
M1_En = 21
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
M1_Vitesse = GPIO.PWM(M1_En, 100)
M1_Vitesse.start(100)


def sens1() :
    GPIO.output(Pins[0], GPIO.HIGH)
    GPIO.output(Pins[1], GPIO.LOW)
    print("Moteur tourne dans le sens 1.")


def sens2() :
    GPIO.output(Pins[0], GPIO.LOW)
    GPIO.output(Pins[1], GPIO.HIGH)
    print("Moteur tourne dans le sens 2.")
    
def arret() :
    GPIO.output(Pins[0], GPIO.LOW)
    GPIO.output(Pins[1], GPIO.LOW)
    print("Moteur s'arrete.")

while True :
    # Exemple de motif de boucle
    sens1()
    sleep(2)

    sens2()
    sleep(2)
