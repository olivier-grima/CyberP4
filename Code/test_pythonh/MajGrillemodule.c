#include <Python.h>
#include "strat_jeu.h"

static PyObject *MAJ_GrilleFunc(PyObject* self, PyObject* args){
    int coup;
    int statut;
    char jeton;
    struct position pos;

    if(!PyArg_ParseTuple(args, "is", &coup, &jeton)){
        return NULL;
    }
    //on print le joueur venant de jouere et la colonne jouée par le joueur
    printf("Le joueur %c a joué : %d\n", jeton, coup + 1);
    //on convertit en la position correspondante dans la grille
    calcule_position(coup, &pos);
    //on met a jour la grille
    grille[pos.colonne][pos.ligne] = jeton;
    //on affiche la grille sur le terminal
    affiche_grille();
    //on verifie l'etat du jeu
    statut = statut_jeu(&pos, jeton);
    if (statut == STATUT_GAGNE)
        printf("Le joueur %d a gagné\n", (jeton == J1_JETON) ? 1 : 2);
    else if (statut == STATUT_EGALITE)
        printf("Égalité\n");
    //c'est au joueur adverse de jouer
    PLAYER = (jeton == J1_JETON) ? J2_JETON : J1_JETON; 
}

static PyMethodDef IaMethods[] = 
{
    {"MAJ_GrilleFunc", MAJ_GrilleFunc, METH_VARARGS, "mets à jour la grille"},
    {NULL, NULL, 0, NULL}
};

static struct PyModuleDef MajGrille_module ={
    PyModuleDef_HEAD_INIT,
    "MajGrille", 
    NULL,
    -1,
    IaMethods
};

PyMODINIT_FUNC PyInit_somme(void){
    return PyModule_Create(&MajGrille_module);
}