#include <Python.h>
#include "strat_jeu.h"

static PyObject *iaFunc(PyObject* self, PyObject* args){

    int meilleurs_col[P4_COLONNES];
    int nb_meilleurs_col = 0;
    int max = 0;
    int col;
    int resultat;
    FILE *fptr;
    fptr = fopen("newTab.txt", "w");
    fprintf(fptr,"%c\n", 'c');
    fprintf(fptr,"%c\n", grille[0][0]);
    fprintf(fptr,"%c\n", grille[1][0]);
    fprintf(fptr,"%c\n", grille[2][0]);
    fprintf(fptr,"%c\n", grille[3][0]);
  /* fprintf(fptr,"%c\n", grille[4][0]);
    fprintf(fptr,"%c\n", grille[5][0]);
    fprintf(fptr,"%c\n", grille[6][0]);
    fprintf(fptr,"%c\n", grille[0][1]);
    fprintf(fptr,"%c\n", grille[2][1]);
    fprintf(fptr,"%c\n", grille[3][1]);
    fprintf(fptr,"%c\n", grille[4][1]);
    fprintf(fptr,"%c\n", grille[5][1]);
    fprintf(fptr,"%c\n", grille[6][1]);
    fprintf(fptr,"%c\n", grille[6][1]);
    fprintf(fptr,"%c\n", grille[0][2]);
    fprintf(fptr,"%c\n", grille[1][2]);
    fprintf(fptr,"%c\n", grille[2][2]);
    fprintf(fptr,"%c\n", grille[3][2]);
    fprintf(fptr,"%c\n", grille[4][2]);
    fprintf(fptr,"%c\n", grille[5][2]);
    fprintf(fptr,"%c\n", grille[6][2]);
    fprintf(fptr,"%c\n", grille[0][3]);
    fprintf(fptr,"%c\n", grille[1][3]);
    fprintf(fptr,"%c\n", grille[2][3]);
    fprintf(fptr,"%c\n", grille[3][3]);
    fprintf(fptr,"%c\n", grille[4][3]);
    fprintf(fptr,"%c\n", grille[5][3]);
    fprintf(fptr,"%c\n", grille[6][3]);
    fprintf(fptr,"%c\n", grille[0][4]);
    fprintf(fptr,"%c\n", grille[1][4]);
    fprintf(fptr,"%c\n", grille[2][4]);
    fprintf(fptr,"%c\n", grille[3][4]);
    fprintf(fptr,"%c\n", grille[4][4]);
    fprintf(fptr,"%c\n", grille[5][4]);
    fprintf(fptr,"%c\n", grille[6][4]);
    fprintf(fptr,"%c\n", grille[0][5]);
    fprintf(fptr,"%c\n", grille[1][5]);
    fprintf(fptr,"%c\n", grille[2][5]);
    fprintf(fptr,"%c\n", grille[3][5]);
    fprintf(fptr,"%c\n", grille[4][5]);
    fprintf(fptr,"%c\n", grille[5][5]);
    fprintf(fptr,"%c\n", grille[6][5]);*/
    for (col = 0; col < P4_COLONNES; ++col)
    {
        struct position pos;
        int longueur;
        
        
        if (grille[col][0] != ' ')
            continue;

        calcule_position(col, &pos);
        longueur = calcule_nb_jetons_depuis(&pos, J2_JETON);
        //fprintf(fptr,"longueur de %d\n", 1);
        if (longueur >= 4)
            return Py_BuildValue("i", col);

        longueur = umax(longueur, calcule_nb_jetons_depuis(&pos, J1_JETON));

        if (longueur >= max)
        {
            if (longueur > max)
            {
                nb_meilleurs_col = 0;
                max = longueur;
            }

            meilleurs_col[nb_meilleurs_col++] = col;
        }
    }
    resultat = meilleurs_col[0];
    //fprintf(fptr,"resultat %d",resultat);
    fclose(fptr);
    //resultat = meilleurs_col[2];
    //return Py_BuildValue("i",meilleurs_col[nb_aleatoire_entre(0, nb_meilleurs_col - 1)]);
    return Py_BuildValue("i", resultat);
    
}

static PyMethodDef IaMethods[] = 
{
    {"iaFunc", iaFunc, METH_VARARGS, "fais plus 6"},
    {NULL, NULL, 0, NULL}
};

static struct PyModuleDef ia_module ={
    PyModuleDef_HEAD_INIT,
    "ia", 
    NULL,
    -1,
    IaMethods
};

PyMODINIT_FUNC PyInit_ia(void){
    return PyModule_Create(&ia_module);
}