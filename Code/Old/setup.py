from setuptools import setup, Extension

setup(
	ext_modules=[Extension('somme', ['sommemodule.c'])],
)