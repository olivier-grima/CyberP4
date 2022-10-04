import RPi.GPIO as GPIO
import time
from time import sleep

#--------------------------- INITIALISATIONS -------------------------------
#
player=0
#-----------------------------SERVO-------------------------
GPIO.setmode(GPIO.BCM)
GPIO.setup(12, GPIO.OUT)
GPIO.setwarnings(True)

ajoutAngle = 5

angle1 = 90;
angle2 = 180;
duree = 2;
duree2 = 0.5;


angleChoisi1 = angle1/10 + ajoutAngle
angleChoisi2 = angle2/10 + ajoutAngle

pwm=GPIO.PWM(12,100)
#-----------------------------MOTEUR-------------------------
# Definition des pins
M1_En = 13
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

#reglage du PWM
M1_Vitesse = GPIO.PWM(M1_En,80)
M1_Vitesse.start(100)

#-----------------------------FIN DE COURSE---------------------
fin_de_course= 14
GPIO.setup(fin_de_course, GPIO.IN)

#--------------------------------CAPTEUR EFFET HALL----------------------------------
#Initialization
HALL_SENSOR= 7 #Penser a le changer
GPIO.setmode(GPIO.BCM)
GPIO.setup(HALL_SENSOR, GPIO.IN, pull_up_down=GPIO.PUD_UP)
cpt =0   #compteur d'aimants

#------------------------------ CAPTEURS IR ----------------------------------
col1=25
col2=6
col3=26
col4=17
col5=27
col6=22
col7=23
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

#--------- CAPTEUR EFFET HALL --------
def passage_aimant(channel):
    global cpt
    cpt += 1
    print("detection de ", cpt, " aimant")

def goRow(r):
    global cpt
    while(cpt!=r):
        sens2()
    cpt=0
    arret()
     
#---------CAPTEURS IR ----------------
def passage_jeton(channel):
    global player
    switcher = {
        25 : "colonne 1",
        6 : "colonne 2",
        26 : "colonne 3",
        17 : "colonne 4",
        27 : "colonne 5",
        22 : "colonne 6",
        23 : "colonne 7",
    }
    #print(switcher.get(channel,"Colonne invalide"))
    player=1
    
def drop():
    pwm.start(5)
    pwm.ChangeDutyCycle(angleChoisi1)
    time.sleep(duree2)
    pwm.ChangeDutyCycle(angleChoisi2)
    time.sleep(duree2)
    pwm.ChangeDutyCycle(0)
    #pwm.stop()
    print("jeton laché")
    

GPIO.add_event_detect(HALL_SENSOR, GPIO.FALLING, callback=passage_aimant, bouncetime=100)
GPIO.add_event_detect(col1, GPIO.FALLING, callback=passage_jeton, bouncetime=100)
GPIO.add_event_detect(col2, GPIO.FALLING, callback=passage_jeton, bouncetime=100)
GPIO.add_event_detect(col3, GPIO.FALLING, callback=passage_jeton, bouncetime=100)
GPIO.add_event_detect(col4, GPIO.FALLING, callback=passage_jeton, bouncetime=100)
GPIO.add_event_detect(col5, GPIO.FALLING, callback=passage_jeton, bouncetime=100)
GPIO.add_event_detect(col6, GPIO.FALLING, callback=passage_jeton, bouncetime=100)
GPIO.add_event_detect(col7, GPIO.FALLING, callback=passage_jeton, bouncetime=100)
    
while(True):
    fin =GPIO.input(fin_de_course)
    
    sens1()
    #print(fin)
    if(fin):
        for i in range(7):
            cpt=0
            goRow(i+1)
            print("Colonne", i)
            drop()
            #sleep(2)
            sens1()
            print("fin course")
            #sens2()
            sleep(2)
            i = i+ 1
    #if(player):
        #goRow(2)
    
      
        
        
         
    


