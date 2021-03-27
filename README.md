# FakeOs

- English
- [Spanish](https://github.com/Hint-Box/FakeOS/blob/main/README.es.md)

A user-friendly terminal **simulator** whose purpose is to teach new users about the use of
real terminals (mainly UNIX systems), designed with scalability in mind from the
beginning to ensure the longevity of the project.

# Installation
For install the lastest version of FakeOS, you will nee Python 3.8.9+ y Cython.

#### Install dependencies
For GNU/Linux systems, use the package manager that provide your distribution, if you
do not already have Python installed.

* Debian-based distributions: `sudo apt upgrade && sudo apt install python3 && sudo apt update`
* Arch-based distributions: `sudo pacman -Syu && sudo pacman -S python3`

Next, the Cython installation will be performed. If you have the *pip* Python package
manager, use the `pip install cython` command. If not, use your distribution's built-in
package manager in the same way as shown above, replacing *"python"* with *"pip"*.

#### FakeOS installation
Congratulations! You already have the necessary dependencies to use FakeOS, now the
installation process.

First, download the [lastest version of the program](https://www.github.com/Hint-Box/FakeOS/archive/refs/heads/main.zip "Download Link")
and extract the *zip* file to the directory of your choice.

Now, you need to compile the `translations.pyx` file included with the download. For this,
please refer to this table:

|Cython installed with pip|Cython installed with the A.D.P.|
|---|---|
|`python setup.py build_ext --inplace`|`cythonize -i translations.pyx`|

If it worked properly, you must see a file named *"translations.[YOUR_SYSTEM_INFO].so"* in
the directory where it is located (a directory called *"build"* and a file called
*"translations.c"* will also be created. but they are not relevant).

Finally, for execute FakeOS, use the command `python3 main.py`. Enjoy!

## Additional information
**Status**: Development, unfinished.

**Dependencies**: Python 3.8.9+, Cython 0.29.2+, pip3 (optional).

**Operative System**: GNU/Linux, FreeBSD, UNIX.

_This repository is a complete reimplementation of the [previous version.](https://www.github.com/fabiopolancoe/FakeOS)_

## Credits
**Fabio** (*fabiopolancoe*): CSV Translates file, installations script, general code.

**Sebas** (*Sebastian-byte*): Arguments system, general code.

**FRostri** (*Rubén Zamora*): Documentation, scripting language, general code.

**Suaj** (*SuajCarrot*): Optimization with Cython, general code.
