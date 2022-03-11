#include <Python.h>

static PyObject *sommefunc(PyObject* self, PyObject* args){
    double number;
    double res;

    if(!PyArg_ParseTuple(args, "d", &number)){
        return NULL;
    }
    res = number +6;
    printf("Code C\n");

    return Py_BuildValue("f", res);
}


static PyMethodDef SommeMethods[] = 
{
    {"sommefunc", sommefunc, METH_VARARGS, "fais plus 6"},
    {NULL, NULL, 0, NULL}
};


static struct PyModuleDef somme_module ={
    PyModuleDef_HEAD_INIT,
    "somme", 
    NULL,
    -1,
    SommeMethods
};

static PyObject*
PyInit_somme(void){
    return PyModule_Create(&somme_module);
}



