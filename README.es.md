# FakeOS

- [English](https://github.com/Hint-Box/FakeOS/blob/main/README.md)

Un **simulador** de terminal amigable cuyo propósito es enseñar a los usuarios nuevos sobre el uso
de terminales reales (principalmente de sistemas UNIX), diseñado con la escalabilidad en mente desde
un inicio para garantizar la longevidad del proyecto.

# Instalación
Para instalar la versión actual de FakeOS, necesitará Python 3.8.9+ y Cython.

### Instalación de dependencias
Para sistemas GNU/Linux, utilice el administrador de paquetes que venga con su distribución, si
no es que ya tiene Python instalado.

* Distribuciones basadas en Debian: `sudo apt upgrade && sudo apt install python3 && sudo apt update`
* Distribuciones basadas en Arch: `sudo pacman -Syu && sudo pacman -S python3`

A continuación, se llevará a cabo la instalación de Cython. Si cuenta con el administrador de
paquetes de Python *pip*, utilice el comando `pip install cython`. Si no, use su administrador de
paquetes integrado con su distribución de la misma forma que se mostró anteriormente,
sustituyendo *"python"* por *"python-pip"*.

### Instalación de FakeOS
¡Enhorabuena! Ya cuenta con las dependencias necesarias para usar FakeOS, ahora el proceso de
instalación del mismo.

Primero, descargue la [versión actual del programa](https://www.github.com/Hint-Box/FakeOS/archive/refs/heads/main.zip "Download Link")
y extraiga el archivo *zip* al directorio de su preferencia.

Ahora, se necesita compilar el archivo `translations.pyx` incluido con la descarga.
Para esto, guíese con esta tabla:

|Cython instalado con pip|Cython instalado con el A.D.P.|
|---|---|
|`python setup.py build_ext --inplace`|`cythonize -i translations.pyx`|

Si funcionó correctamente, un archivo llamado *"translations.[INFO_DE_SU_SO].so"* debió
haber sido creado en el directorio donde se encuentra (también se creará un directorio llamado
*"build"* y un archivo llamado *"translations.c"*, pero no son relevantes).

Finalmente, para ejecutar FakeOS utilice el comando `python3 main.py`. ¡Disfrute!

## Información adicional
**Estado**: En desarrollo, incompleto.

**Dependencias**: Python 3.8.9+, Cython 0.29.2+, pip3 (opcional).

**Sistema Operativo**: GNU/Linux, FreeBSD, UNIX.

_Este repositorio es una reescritura completa de la [versión anterior.](https://www.github.com/fabiopolancoe/FakeOS)_


### Créditos
**Fabio** (*fabiopolancoe*): Archivo de traducciones CSV, script de instalación, código en general.

**Sebas** (*Sebastian-byte*): Sistema de argumentos, código en general.

**FRostri** (*Rubén Zamora*): Documentación, lenguaje de scripting, código en general.

**Suaj** (*SuajCarrot*): Optimización con Cython, código en general.
