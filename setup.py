from setuptools import setup
from Cython.Build import cythonize


setup(
    name="Translation Module",
    ext_modules=cythonize(
        "translations.pyx",
        language_level=3,
        annotate=True  # Generate an HTML file with info, only for debugging
    ),
    zip_safe=False
)
