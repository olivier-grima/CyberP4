import ctypes as ct

_lib = ct.cdll.LoadLibrary("./connect4Bis.so")

# Utilisation
_lib.faitout()
