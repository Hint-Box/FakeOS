# FakeOS

* [Español](https://github.com/Hint-Box/FakeOS/blob/main/README.es.md)

A user-friendly terminal **simulator** whose purpose is to teach new users about the use of
real terminals (mainly UNIX systems), designed with scalability in mind from the
beginning to ensure the longevity of the project.

# Installation
To install the latest version of FakeOS, you will need Python 3.8.9+ and Cython.

### Dependencies installation
For GNU/Linux systems, use the package manager that your distribution provides, if you
do not already have Python installed.

* Debian-based distributions: `sudo apt upgrade && sudo apt install python3 && sudo apt update`
* Arch-based distributions: `sudo pacman -Syu && sudo pacman -S python3`

Next, the Cython installation will be performed. If you have the *pip* Python package
manager, use the `pip install cython` command. If you don't, use your distribution's default
package manager in the same way as shown above, replacing *"python"* with *"pip"*.

### FakeOS installation
Congratulations! Now you have the necessary dependencies to use FakeOS, now comes the
installation process.

First, download the [latest version of the program](https://www.github.com/Hint-Box/FakeOS/archive/refs/heads/main.zip "Download Link")
and extract the *zip* file to the directory of your choice.

Now, you need to compile the `translations.pyx` file included with the download. To do this,
check this table:

|Cython installed with pip|Cython installed with the P.M.|
|---|---|
|`python setup.py build_ext --inplace`|`cythonize -i translations.pyx`|

If it worked properly, you should see a file named *"translations.[YOUR_OS_INFO].so"* in
the directory where you are located (a directory called *"build"* and a file called
*"translations.c"* will also be created, but they are not relevant).

Finally, to execute FakeOS use the command `python3 main.py`. Enjoy!

## Additional information
**Status**: In development, incomplete.

**Dependencies**: Python 3.8.9+, Cython 0.29.2+, pip3 (optional).

**Operative System**: GNU/Linux, FreeBSD, UNIX.

_This repository is a complete rewrite of the [previous version.](https://www.github.com/fabiopolancoe/FakeOS)_

## Credits
**Fabio** (*fabiopolancoe*): CSV translations file, installation script, general code.

**Sebas** (*Sebastian-byte*): Arguments system, general code.

**FRostri** (*Rubén Zamora*): Documentation, scripting language, general code.

**Suaj** (*SuajCarrot*): Cython optimization, general code.
