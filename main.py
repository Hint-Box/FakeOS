#!/usr/bin/env python3

import sys  # Will be widely used in all the program
import os
import locale

import csv  # Used for translation system
import urllib.request  # Used for downloading data

from os.path import join as join_dirs
from os.path import isfile as is_file
from os.path import isdir as is_dir
from getpass import getuser  # Used to obtain the username for the shell

from translations import HumanLanguage

user = getuser()


data_path = join_dirs(os.path.expanduser("~"), ".local", "FakeOS")
languages_path = join_dirs(data_path, "languages.csv")

def command_handler(command):
    try:
        returned_value = command_dict[command]()
        return returned_value
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
        if command in {"-c", "--command"} \
        and argv[index + 2] not in {"-c", "--command"}
    )
    return returned_values


def main():
    # Detect default language and initialize LoadHumanLanguage class with it
    loc = locale.getdefaultlocale()[0]
    if loc.startswith("en"):
        l = HumanLanguage("English", languages_path)
    elif loc.startswith("es"):
        l = HumanLanguage("Spanish", languages_path)
    elif loc.startswith("eo"):
        l = HumanLanguage("Esperanto", languages_path)
    
    print(f"\n{l.get('welcome_msg')}\n")
    
    while(True):
        command = input(f"{user}@FakeOS$ ")
        command_handler(command)

def exit_shell():
    sys.exit()

command_dict = {
    "exit": exit_shell
}

if __name__ == "__main__":
    main()

