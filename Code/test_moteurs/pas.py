
#!/usr/bin/env python
# -*- coding: latin-1 -*-

'''
Contrôle d'un moteur pas avec un Raspberry Pi
L'utilisateur choisit le nombre de pas qui sera fait par le moteur
http://electroniqueamateur.blogspot.com/2014/12/controle-dun-moteur-pas-pas-par-un.html
'''

import RPi.GPIO as GPIO
import time
     
GPIO.setmode(GPIO.BCM)  #notation board plutôt que BCM
     
pin_bobine_1_1 = 17   #GPIO 22
pin_bobine_1_2 = 27   #GPIO 23
pin_bobine_2_1 = 22   #GPIO 24
pin_bobine_2_2 = 23   #GPIO 25

# configuration des pins en sortie
GPIO.setup(pin_bobine_1_1, GPIO.OUT)
GPIO.setup(pin_bobine_1_2, GPIO.OUT)
GPIO.setup(pin_bobine_2_1, GPIO.OUT)
GPIO.setup(pin_bobine_2_2, GPIO.OUT)

print ("----CONTROLE D'UN MOTEUR PAS A PAS -----")
     
def marche_avant(attente, nombre_de_pas):
    for i in range(0, nombre_de_pas):
        prochainStep(i % 4)
        time.sleep(attente)

def marche_arriere(attente, nombre_de_pas):
    for i in range(0, nombre_de_pas):
        prochainStep(3 - (i % 4))
        time.sleep(attente)

def reglage_pins(pin1, pin2, pin3, pin4):
    GPIO.output(pin_bobine_1_1, pin1)
    GPIO.output(pin_bobine_1_2, pin2)
    GPIO.output(pin_bobine_2_1, pin3)
    GPIO.output(pin_bobine_2_2, pin4)

def prochainStep(numero):
    if (numero == 0):
        reglage_pins(1, 0, 1, 0)
    if (numero == 1):
        reglage_pins(0, 1, 1, 0)
    if (numero == 2):
        reglage_pins(0, 1, 0, 1)
    if (numero == 3):
        reglage_pins(1, 0, 0, 1)
     
while True:
    print ("Le delai entre chaque pas permet de controler la vitesse du moteur.")
    print ("Entrez une valeur d'au moins 5 millisecondes (rotation tres rapide).")
    attente = input("Delai desire:  ")
    print ("Choisissez le nombre de pas accomplis par le moteur.")
    print ("(Une valeur negative fera tourner le moteur en sens inverse.)")
    nombre_de_pas = input("Nombre de pas desire:  ")
    if (int(nombre_de_pas) < 0):
        marche_arriere(int(attente) / 1000.0, -int(nombre_de_pas))
    else:
        marche_avant(int(attente) / 1000.0, int(nombre_de_pas))
    continuer = input("Desirez-vous encore faire tourner le moteur? (o ou n)")
    if (continuer == 'n'):
        break;
print ("Au revoir!")
GPIO.cleanup()

