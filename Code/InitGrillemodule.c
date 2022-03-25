#include <Python.h>
#include "strat_jeu.h"

static PyObject *init_GrilleFunc(PyObject* self, PyObject* args){
    unsigned col;
    unsigned lgn;
    
    if(!PyArg_ParseTuple(args, "ii", &col, &lgn)){
        return NULL;
    }

    for (col = 0; col < P4_COLONNES; ++col)
        for (lgn = 0; lgn < P4_LIGNES; ++lgn)
            grille[col][lgn] = 'c';

    Py_RETURN_NONE;
}

static PyMethodDef InitGrille_Methods[] = 
{
    {"init_GrilleFunc", init_GrilleFunc, METH_VARARGS, "initialise la grille"},
    {NULL, NULL, 0, NULL}
};

static struct PyModuleDef InitGrille_module ={
    PyModuleDef_HEAD_INIT,
    "InitGrille", 
    NULL,
    -1,
    InitGrille_Methods
};

PyMODINIT_FUNC PyInit_InitGrille(void){
    return PyModule_Create(&InitGrille_module);
}