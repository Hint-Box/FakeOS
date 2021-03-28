#!/usr/bin/env python3
"""
Functions:
    command_handler(command) -> Optional[Any]
    sys_command_handler() -> tuple
    main() -> None
"""

from locale import getdefaultlocale
from typing import Optional, Any
from getpass import getuser
import sys

try:
    from translations import HumanLanguage
except ModuleNotFoundError:
    try:  # Use pyximport to automatically compile the Cython modules
        import pyximport

        pyximport.install()
        from translations import HumanLanguage
    except ImportError as id:
        print(
            "FATAL ERROR: Could not load the Cython modules required to run\
the program. Try compiling them manually."
        )
        print(f"Exception Details: {id}")

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
        if command in {"-c", "--command"} and argv[index + 2] not in {"-c", "--command"}
    )
    return returned_values


def main() -> None:
    """
    Detect default language and initialize HumanLanguage class with it

    :return: The function don't return anything
    :rtype: None
    """

    user = getuser()

    syslocale = getdefaultlocale()[0][:2]
    try:
        lang = {"en": "English", "es": "Spanish", "eo": "Esperanto"}[syslocale]
    except KeyError:
        lang = "English"  # Default language
    msg = HumanLanguage(bytes(lang, "utf-8"))

    print("\n" + msg.get("welcome"))
    print(msg.get("version"), str(version), "\n")

    try:
        while True:
            command_handler(input(f"[{user}@FakeOS]$ "))
    except KeyboardInterrupt:
        print("\n" + msg.get("close"))
        sys.exit(0)


command_dict = {
    "exit": sys.exit,
}

if __name__ == "__main__":
    main()
