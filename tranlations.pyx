#!/usr/bin/env python3

# Main module. The commands (see the future commands.py module), menu and
# configuration are handled here.

from locale import getdefaultlocale
import sys

from os.path import join as join_dirs
from os.path import isfile as is_file
from os.path import isdir as is_dir
from getpass import getuser

from translations import HumanLanguage


def command_handler(command):
    # TO-DO: HACER EL SISTEMA DE ARGUMENTOS
    try:
        return command_dict[command]()  # Return whatever the func returned
    except (KeyError, IndexError, NameError):
        try:
            exec(f"from apps import {command}")
        except ImportError:
            print("Sorry, we couldn't recognize that command.")


def sys_command_handler():
    argv = sys.argv[1:]

    # NOTA: Mejorar esto

    # Create a generator of the returned values of each function
    # called in the system arguments

    # To add arguments to a function called there, use _
    # instead of spaces
    # Example: To call "echo "EOF" >> file.txt":
    # $ python main.py -c echo EOF_>>_file.txt

    # If a function doesn't have arguments, use -c again to
    # delimit it.
    # Example: To call "ls":
    # $ python main.py -c ls -c

    returned_values = (
        command_handler(argv[index + 1], *argv[index + 2].split("_"))
        for index, command in enumerate(argv)
        if command in {"-c", "--command"}
        and argv[index + 2] not in {"-c", "--command"}
    )
    return returned_values


def main():
    user = getuser()

    # Detect default language and initialize LoadHumanLanguage class with it
    syslocale = getdefaultlocale()[0][2:]
    try:
        lang = {"en": "English", "es": "Spanish", "eo": "Esperanto"}[syslocale]
    except KeyError:
        lang = "English"  # Default language
    msg = HumanLanguage(bytes(lang, "utf-8"))

    print("\n", msg.get('welcome_msg'), "\n")

    while(True):
        command_handler(input(f"{user}@FakeOS> "))


command_dict = {
    "exit": sys.exit(0)
}

if __name__ == "__main__":
    main()