from setuptools import setup, Extension

setup(
	ext_modules=[Extension('MajGrille', ['MajGrillemodule.c'])],
)