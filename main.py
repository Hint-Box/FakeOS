#!/usr/bin/env python3

import sys
import os
import locale
import signal # Used to handle SIGINT

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
    # Detect default language and initialize HumanLanguage class with it
    loc = locale.getdefaultlocale()[0]
    if loc.startswith("es"):
        msg = HumanLanguage(b"Spanish", languages_path.encode())
    elif loc.startswith("eo"):
        msg = HumanLanguage(b"Esperanto", languages_path.encode())
    else:
        msg = HumanLanguage(b"English", languages_path.encode())
        
	# Code to run if user presses Ctrl+C key combo
    def signal_handler(sig, frame):
	    try:
		    print("\n"+msg.get('close'))
		    sys.exit(0)
	    except NameError:
		    print("\nLeaving...")
		    sys.exit(0)
		    
	# Listen for Ctrl+C and execute funcion above if it happens
    signal.signal(signal.SIGINT, signal_handler)
    
    print(f"\n{msg.get('welcome')}, {user}!")
    print(msg.get("version"))    
    
    while(True):
        command = input(f"\n{user}@FakeOS$ ")
        command_handler(command)

def exit_shell():
    sys.exit()

def numguess():
    print(msg.get("numguess_welcome"))

command_dict = {
    "exit": exit_shell,
    "num-guess": numguess
}

if __name__ == "__main__":
    main()

