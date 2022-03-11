#pragma once

#include <ctype.h>
#include <stddef.h>
#include <stdio.h>
#include <stdlib.h>

#define P4_COLONNES (7)
#define P4_LIGNES (6)

#define J1_JETON ('O')
#define J2_JETON ('X')


#define ACT_ERR (0)
#define ACT_JOUER (1)
#define ACT_NOUVELLE_SAISIE (2)
#define ACT_QUITTER (3)

#define STATUT_OK (0)
#define STATUT_GAGNE (1)
#define STATUT_EGALITE (2)

struct position
{
    int colonne;
    int ligne;
};

char PLAYER='O';

static void affiche_grille(void);
static void calcule_position(int, struct position *);
static unsigned calcule_nb_jetons_depuis_vers(struct position *, int, int, char);
static unsigned calcule_nb_jetons_depuis(struct position *, char);
//static int coup_valide(int);
//static int demande_action(int *);
//static int demande_nb_joueur(void);
static int grille_complete(void);
//static int ia(void);
static void initialise_grille(void);
double nb_aleatoire(void);
int nb_aleatoire_entre(int, int);
static int position_valide(struct position *);
static int statut_jeu(struct position *pos, char);
static unsigned umax(unsigned, unsigned);
//static int vider_tampon(FILE *);
void maj_grille_terminal(int coup, char jeton);
void start();
static char grille[P4_COLONNES][P4_LIGNES];