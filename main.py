#!/usr/bin/env python3
"""
Main module. The commands (see the future commands.py module), menu and
configuration are handled here.

Functions:

    command_handler(command) -> Optional[Any]
    sys_command_handler() -> tuple
    main() -> None
"""

from locale import getdefaultlocale
import sys

from os.path import join as join_dirs
from os.path import isfile as is_file
from os.path import isdir as is_dir
from getpass import getuser
from typing import Optional, Any

from translations import HumanLanguage

version = 2.0  # Just for testing


def command_handler(command: str) -> Optional[Any]:
    """
    Execute the command that matches one of those in command_dict.

    :param command: The command to be executed
    :type command: str
    :return: The function can return anything the command return or None
    :rtype: Optional[Any]
    """

    # TODO: HACER EL SISTEMA DE ARGUMENTOS
    try:
        return command_dict[command]()  # Return whatever the func returned
    except (KeyError, IndexError, NameError):
        try:
            exec(f"from apps import {command}")
        except ImportError:
            print("Sorry, we couldn't recognize that command.")


def sys_command_handler() -> tuple:
    """
    Create a generator of the returned values of each func called in the
    system arguments.

    To add arguments to a function called there, use _ instead of spaces.
    Example: To call "echo "EOF" >> file.txt":
    $ python main.py -c echo EOF_>>_file.txt

    If a function doesn't have arguments, use -c again to delimit it.
    Example: To call "ls":
    $ python main.py -c ls -c

    :return: Return a tuple with the value of each returned vaule of each
    command called
    :rtype: tuple
    """

    argv = sys.argv[:1]

    returned_values = (
        command_handler(argv[index + 1], *argv[index + 2].split("_"))
        for index, command in enumerate(argv)
        if command in {"-c", "--command"}
        and argv[index + 2] not in {"-c", "--command"}
    )
    return returned_values


def main() -> None:
    """
    Detect default language and initialize HumanLanguage class with it

    :return: The function don't return anything
    :rtype: None
    """

    user = getuser()

    # Detect default language and initialize LoadHumanLanguage class with it
    syslocale = getdefaultlocale()[0][:2]
    try:
        lang = {"en": "English", "es": "Spanish", "eo": "Esperanto"}[syslocale]
    except KeyError:
        lang = "English"  # Default language
    msg = HumanLanguage(bytes(lang, "utf-8"))

    print("\n"+msg.get("welcome"))
    print(msg.get("version"), str(version), "\n")

    try:
        while(True):
            command_handler(input(f"[{user}@FakeOS]$ "))
    except KeyboardInterrupt:
        print("\n"+msg.get("close"))
        sys.exit(0)


command_dict = {
    "exit": sys.exit
}

if __name__ == "__main__":
    main()
