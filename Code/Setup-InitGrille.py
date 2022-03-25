from setuptools import setup, Extension

setup(
	ext_modules=[Extension('InitGrille', ['InitGrillemodule.c'])],
)