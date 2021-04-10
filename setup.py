# Set up file used to build the Cython modules.

from setuptools import setup
from Cython.Build import cythonize

setup(
    name="Translations Module",
    ext_modules=cythonize(
        "translations.pyx",
        language_level=3,
        # annotate=True  # Only for debugging, generates an HTML file
    ),
    zip_safe=False
)
