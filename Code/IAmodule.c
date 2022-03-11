#include <Python.h>
#include "strat_jeu.h"
static PyObject *iaFunc(PyObject* self, PyObject* args){

    unsigned meilleurs_col[P4_COLONNES];
    unsigned nb_meilleurs_col = 0;
    unsigned max = 0;
    unsigned col;

     for (col = 0; col < P4_COLONNES; ++col)
    {
        struct position pos;
        unsigned longueur;

        if (grille[col][0] != ' ')
            continue;

        calcule_position(col, &pos);
        longueur = calcule_nb_jetons_depuis(&pos, J2_JETON);

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
   
    return Py_BuildValue("i", meilleurs_col[nb_aleatoire_entre(0, nb_meilleurs_col - 1)]);
}



static PyMethodDef IaMethods[] = 
{
    {"iafunc", iaFunc, METH_VARARGS, "fais plus 6"},
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