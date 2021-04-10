#!/usr/bin/env python3

# Main module. Most functions from other modules get imported and used here.

# Copyright (C) 2021, DaBitwiseWay team
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see
# https://www.gnu.org/licenses/gpl-3.0.en.html.

"""
Functions:
    command_handler(command) -> Optional[Any]
    sys_command_handler() -> tuple
    main() -> None
"""

from locale import getdefaultlocale
from typing import Optional, Any
import sys
import os

try:
    from translations import HumanLanguage

except (ModuleNotFoundError, ImportError):
    try:  # Use pyximport to automatically compile the Cython modules
        import pyximport
        pyximport.install()
        from translations import HumanLanguage

    except (ModuleNotFoundError, ImportError) as id:
        try:  # Run the command to compile the Cython modules with os.system
            os.system("python3 setup.py build_ext --inplace")
            from translations import HumanLanguage

        except (ModuleNotFoundError, ImportError, OSError):
            print("FATAL ERROR: Could not load the Cython modules required to\
 run the program. Try compiling them manually.")
            print(f"Exception Details: {id}")
            sys.exit(0)


def command_handler(user_input: str) -> Optional[Any]:
    """
    Call the specified function in command_dict.

    :param command: The command to be executed
    :type command: str
    :return: The function can return anything the command return or None
    :rtype: Optional[Any]
    """

    command = user_input.split()[0]
    args = user_input.split()[:1]

    try:
        return command_dict[command](*args)  # Return the returned value
    except (KeyError, IndexError, NameError):
        print("Sorry, we couldn't recognize that command.")


# TODO: THIS FUNCTION
def sys_command_handler() -> tuple:
    """
    Return a tuple of the returned values of each function called in the
    system arguments with the -c flag.

    For example: python main.py -c ls

    If the function has its own arguments, use the -a flag.

    For example: python main.py -c cp -a file1.txt -a file2.txt

    :return: Return a tuple with the value of each returned vaule of each
    command called
    :rtype: tuple
    """

    # argv = sys.argv[:1]

    # for index, value in enumerate(argv):

    # return returned_values


def main() -> None:
    """
    Detect the system's locale and initialize translations.Idiom with it,
    otherwise use English. Also handles the input.

    :return: The function don't return anything
    :rtype: None
    """

    # Idiom set up

    # getdefaultlocale returns a tuple of two elements, but we only care about
    # the first two characters of the first element
    syslocale = getdefaultlocale()[0][:2]
    try:
        idiom = {
            "en": "English",
            "es": "Spanish",
            "eo": "Esperanto"
        }[syslocale]
    except KeyError:
        idiom = "English"  # Default language
    msg = HumanLanguage(bytes(idiom, "utf-8"))

    # Welcome message

    print(f"\n{msg.get('welcome')}\n")
    print(msg.get('version').format("PRE-ALPHA 0.2"))

    # User input

    while True:
        command_handler(input("FakeOS> "))


# TODO: Commands module, this dictionary should also get imported from there
command_dict = {
    "exit": sys.exit,
}

if __name__ == "__main__":
    main()
