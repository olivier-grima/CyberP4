import RPi.GPIO as GPIO
from RpiMotorLib import RpiMotorLib
import time
from time import sleep
import ctypes as ct


#--------------------------- INITIALISATIONS -------------------------------
J1_JETON='O'
J2_JETON='X'
global player
global statut
#------------------------------setup library-------------------------------

_lib = ct.cdll.LoadLibrary("./connect4_py.so")
#return type de ia
_lib.ia.restype = ct.c_int
_lib.update.restype = ct.c_int
_lib.update.argtypes = [ct.c_int, ct.c_wchar]

#-----------------------------SERVO-------------------------
GPIO.setmode(GPIO.BCM)
GPIO.setup(12, GPIO.OUT)
GPIO.setwarnings(True)

ajoutAngle = 5

angle1 = 90
angle2 = 180
duree = 2
duree2 = 1.5


angleChoisi1 = angle1/10 + ajoutAngle
angleChoisi2 = angle2/10 + ajoutAngle

pwm=GPIO.PWM(12,100)
#-----------------------------MOTEUR-------------------------
# Definition des pins
M1_En = 13
M1_In1 = 19
M1_In2 = 26

# Creation d'une liste des pins pour chaque moteur pour compacter la suite du code
Pins = [M1_In1, M1_In2]

# Setup
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(M1_En, GPIO.OUT)
GPIO.setup(M1_In1, GPIO.OUT)
GPIO.setup(M1_In2, GPIO.OUT)

#reglage du PWM
M1_Vitesse = GPIO.PWM(M1_En,80)
M1_Vitesse.start(100)


#-----------------------------STEPPER--------------------

#define GPIO pins
direction = 15     #Direction (DIR) GPIO Pin
step = 18        #Step GPIO Pin
EN_pin = 14      #enable pin (LOW to enable)

mymotortest = RpiMotorLib.A4988Nema(direction, step, (False,False,False), "DRV8825")
GPIO.setup(EN_pin, GPIO.OUT)

#-----------------------------SERVO2-------------------------
servoPIN = 21
GPIO.setmode(GPIO.BCM)
GPIO.setup(servoPIN, GPIO.OUT)

p = GPIO.PWM(servoPIN, 50) # GPIO 17 for PWM with 50Hz


#-----------------------------FIN DE COURSE---------------------
fin_de_course= 20
GPIO.setup(fin_de_course, GPIO.IN)

#--------------------------------CAPTEUR EFFET HALL----------------------------------
#Initialization
HALL_SENSOR= 2 #Penser a le changer
GPIO.setmode(GPIO.BCM)
GPIO.setup(HALL_SENSOR, GPIO.IN, pull_up_down=GPIO.PUD_UP)
cpt =0   #compteur d'aimants

#------------------------------ CAPTEURS IR ----------------------------------
col1=23
col2=24
col3=6
col4=5
col5=22
col6=27
col7=17
GPIO.setmode(GPIO.BCM)
GPIO.setup(col1, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(col2, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(col3, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(col4, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(col5, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(col6, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(col7, GPIO.IN, pull_up_down=GPIO.PUD_UP)


#---------------------------- DEF DES FONCTIONS ----------------------
#--- MOTEUR ----
def sens1() :
    GPIO.output(Pins[0], GPIO.HIGH)
    GPIO.output(Pins[1], GPIO.LOW)
    #print("Moteur tourne dans le sens 1.")

def sens2() :
    GPIO.output(Pins[0], GPIO.LOW)
    GPIO.output(Pins[1], GPIO.HIGH)
    #print("Moteur tourne dans le sens 2.")
    
def arret() :
    GPIO.output(Pins[0], GPIO.LOW)
    GPIO.output(Pins[1], GPIO.LOW)
    #print("Moteur s'arrete.")
    
    
#-------------- STEPPER --------------
def load(direction, steps):
    GPIO.output(EN_pin, GPIO.LOW)
    mymotortest.motor_go(direction,
                         "Full",
                          steps,
                         .005,
                         False,
                         .05) #1er false = monte
    GPIO.output(EN_pin, GPIO.HIGH)


#--------- CAPTEUR EFFET HALL --------
def passage_aimant(channel):
    global cpt
    cpt += 1
    #print("detection de ", cpt, " aimant")

def goRow(r):
    global cpt
    while(cpt!=r):
        sens2()
    arret()
     
#---------CAPTEURS IR ----------------
def passage_jeton(channel):
    colonne = 0
    global player
    if(channel==23):
        statut = _lib.update(1, player)
    if(channel==24):
        statut = _lib.update(2, player)
    if(channel==6):
        statut = _lib.update(3, player)
    if(channel==5):
        statut = _lib.update(4, player)
    if(channel==22):
        statut = _lib.update(5, player)
    if(channel==27):
        statut = _lib.update(6, player)
    if(channel==17):
        statut = _lib.update(7, player)
    print("statut jeu :" ,statut)
    #switcher = {
     #   25 : _lib.update(1, player),
    #   6 : _lib.update(2, player),
     #   26 : _lib.update(3, player),
     #   17 : _lib.update(4, player),
     #   27 : _lib.update(5, player),
     #   22 : _lib.update(6, player),
     #   23 : _lib.update(7, player),
    #}
    player = J1_JETON if (player==J2_JETON) else J2_JETON

    
def drop():
    pwm.start(5)
    pwm.ChangeDutyCycle(angleChoisi1)
    time.sleep(duree2)
    pwm.ChangeDutyCycle(angleChoisi2)
    time.sleep(duree2)
    pwm.ChangeDutyCycle(0)
    #pwm.stop()
    #print("jeton laché")
    
    
def pushTouillette():
    p.start(5) 
    p.ChangeDutyCycle(0)
    p.ChangeDutyCycle(5.5)
    time.sleep(0.5)
    p.ChangeDutyCycle(7)
    time.sleep(0.5)
    p.ChangeDutyCycle(5.5)
    time.sleep(0.5)
    p.ChangeDutyCycle(0)

#---------------------interruptions----------------------------------------
GPIO.add_event_detect(HALL_SENSOR, GPIO.FALLING, callback=passage_aimant, bouncetime=100)
GPIO.add_event_detect(col1, GPIO.FALLING, callback=passage_jeton, bouncetime=100)
GPIO.add_event_detect(col2, GPIO.FALLING, callback=passage_jeton, bouncetime=100)
GPIO.add_event_detect(col3, GPIO.FALLING, callback=passage_jeton, bouncetime=100)
GPIO.add_event_detect(col4, GPIO.FALLING, callback=passage_jeton, bouncetime=100)
GPIO.add_event_detect(col5, GPIO.FALLING, callback=passage_jeton, bouncetime=100)
GPIO.add_event_detect(col6, GPIO.FALLING, callback=passage_jeton, bouncetime=100)
GPIO.add_event_detect(col7, GPIO.FALLING, callback=passage_jeton, bouncetime=100)

#--------------------------------main------------
player=J1_JETON
_lib.debutPartie()
cpt_jetons=0
statut = 0
while(statut == 0):
    #prise position 0...
    fin =GPIO.input(fin_de_course)
    
    if(not fin):
        sens1()
        cpt=0
    else:
        
        if(player == J2_JETON):#quand c'est au tour du robot
            #print("dans le if du python\n")
            load(False,148)
            #sleep(2) pas utile normalement
            pushTouillette()
            col_R = _lib.ia()
            cpt_jetons=cpt_jetons+1
            print("l'ia va jouer dans la colonne : ", col_R, "\n")
            goRow(col_R)
            drop()
            #sens1()
        #elif(statut == 1 or statut == 2):
load(True,1036)

