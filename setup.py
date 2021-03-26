from setuptools import setup
from Cython.Build import cythonize

setup(
    name="Translation Module",
    ext_modules=cythonize("translations.pyx"),
    zip_safe=False
)
