#include <pigpio.h>
#include <stdlib.h>
#include <stdio.h>

/*import RPi.GPIO as GPIO
//from time import sleep

//--------------------------- INITIALISATIONS -------------------------------
#
player=1
//-----------------------------MOTEUR-------------------------
//Definition des pins
M1_En = 13
M1_In1 = 20
M1_In2 = 16

//Creation d'une liste des pins pour chaque moteur pour compacter la suite du code
Pins = [M1_In1, M1_In2]

//Setup
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(M1_En, GPIO.OUT)
GPIO.setup(M1_In1, GPIO.OUT)
GPIO.setup(M1_In2, GPIO.OUT)

#réglage du PWM
M1_Vitesse = GPIO.PWM(M1_En,80)
M1_Vitesse.start(100)

#-----------------------------FIN DE COURSE---------------------
fin_de_course= 14
GPIO.setup(fin_de_course, GPIO.IN)

#--------------------------------CAPTEUR EFFET HALL----------------------------------
#Initialization
HALL_SENSOR= 7 #Penser à le changer
GPIO.setmode(GPIO.BCM)
GPIO.setup(HALL_SENSOR, GPIO.IN, pull_up_down=GPIO.PUD_UP)
cpt =0   #compteur d'aimants

//------------------------------ CAPTEURS IR ----------------------------------
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

*/

//---- Variables statiques ---//

static int M1_En = 13;
static int M1_In1 = 20;
static int M1_In2 = 16;

static int col1=25;
static int col2=6;
static int col3=26;
static int col4=17;
static int col5=27;
static int col6=22;
static int col7=23;

//---------------------------- DEF DES FONCTIONS ----------------------

//--- MOTEUR ----//

void sens1(){
    gpioWrite(20, 1);
    gpioWrite(16, 0);
    printf("Moteur tourne dans le sens 1");
}

void sens2(){
    gpioWrite(20, 0);
    gpioWrite(16, 1);
    printf("Moteur tourne dans le sens 2");
}
    
void arret(){
    gpioWrite(20, 0);
    gpioWrite(16, 0);
    printf("Arrêt");
}

//---- Callbacks ----//

void passage_jeton(int gpio, int level, uint32_t tick){
    switch (gpio) {
        case 25:
            printf("Colonne 1");
            break;
        case 6:
            printf("Colonne 2");
            break;
        case 26:
            printf("Colonne 3");
            break;
        case 17:
            printf("Colonne 4");
            break;
        case 27:
            printf("Colonne 5"); 
            break;
        case 22:
            printf("Colonne 6");
            break;
        case 23:
            printf("Colonne 7");
            break;
        default: 
            printf("Colonne invalide");
        }
    //player = 1;


}

/*--------- CAPTEUR EFFET HALL --------
def passage_aimant(channel):
    global cpt
    cpt += 1
    print("détection de ", cpt, " aimant")

def goRow(r):
    global cpt
    global player
    while(cpt!=r):
        sens2()
    cpt=0
    arret()
    sleep(2)
    player = 0
    sens1()
     
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
    print(switcher.get(channel,"Colonne invalide"))
    player=1
   */ 



    
/*while(True):
    fin =GPIO.input(fin_de_course)
    sens2()
    print(fin)
    if(fin):
        print("fin course")
        sens1()
        sleep(3)
    if(player):
        goRow(2)
    else :*/
        
      
        
        
int main(){
    

    //---- setup ----//

    //GPIO.setmode(GPIO.BCM)
    GpioSetMode(M1_En, PI_OUTPUT);
    GpioSetMode(M1_In1, PI_OUTPUT);
    GpioSetMode(M1_In2, PI_OUTPUT);

    int player=1; //1 = robot 0 = humain

    //---- interruptions ----//

    gpioSetISRFuncEx(col1, FALLING_EDGE, 100, passage_jeton, NULL);
    gpioSetISRFuncEx(col2, FALLING_EDGE, 100, passage_jeton, NULL);
    gpioSetISRFuncEx(col3, FALLING_EDGE, 100, passage_jeton, NULL);
    gpioSetISRFuncEx(col4, FALLING_EDGE, 100, passage_jeton, NULL);
    gpioSetISRFuncEx(col5, FALLING_EDGE, 100, passage_jeton, NULL);
    gpioSetISRFuncEx(col6, FALLING_EDGE, 100, passage_jeton, NULL);
    gpioSetISRFuncEx(col7, FALLING_EDGE, 100, passage_jeton, NULL);



    /*//réglage du PWM
    M1_Vitesse = GPIO.PWM(M1_En,80)
    M1_Vitesse.start(100)

    //-----------------------------FIN DE COURSE---------------------
    fin_de_course= 14
    GPIO.setup(fin_de_course, GPIO.IN)

    #--------------------------------CAPTEUR EFFET HALL----------------------------------
    #Initialization
    HALL_SENSOR= 7 #Penser à le changer
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(HALL_SENSOR, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    cpt =0   #compteur d'aimants*/

    return EXIT_SUCCESS;
}

