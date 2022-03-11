from setuptools import setup, Extension

setup(
	ext_modules=[Extension('ia', ['IAmodule.c'])],
)