from setuptools import setup
from Cython.Build import cythonize

setup(
    name="Translation Module",
    ext_modules=cythonize("translation.pyx"),
    zip_safe=False
)
