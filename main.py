#!/usr/bin/python

from os.path import join as join_dirs
from os.path import isfile as is_file
from os.path import isdir as is_dir
from getpass import getuser  # Used to obtain the username for the shell
import sys  # Will be widely used in all the program
import os

import urllib.request  # Used for downloading data
import csv  # Used for translation system

user = getuser()

command_dict = {
    "s": "s"
}

# Code for translation system
# Check if data folder exists, if it doesn't, create it

def load_human_language():
    data_path = join_dirs(os.path.expanduser("~"), ".local", "FakeOS")
    languages_path = join_dirs(data_path, "languages.csv")

    if not is_dir(data_path):
        try:
            os.makedirs(data_path)
        except OSError as id:
            print(f"Oh, no! An exception occurred. Details: {id}")

    if not is_file(languages_path):
        print("Oh, no! We cannot find the CSV file for other languages, trying to download it...")
        
        try:
            urllib.request.urlretrieve("https://raw.githubusercontent.com/Hint-Box/FakeOS/main/languages.csv",languages_path)
        
        except Exception as id:
            print(f"Oops, we had an error while getting the file, please try\
downloading \"https://raw.githubusercontent.com/Hint-Box/FakeOS/main/\
languages.csv\" manually, then save it to {data_path}.")
            print(f"Details: {id}")

    else:
        try:
            with open(languages_path, "r") as t_file:
                pass  # Code to load the CSV

        except FileNotFoundError:
            print("Oh, no! Something reallly bad happened, we cannot load the translations file and it's\
                impossible to start the program without it, quitting...")
            sys.exit(0)


def command_handler(command, *command_args):
    try:
        returned_value = command_dict[command](*command_args)
    except (KeyError, IndexError):
        print("Sorry, we couldn't recognize that command.")
    else:
        return returned_value


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

    # OTRA NOTA: Hay que recordar que decidimos que en este rewrite, las
    # aplicaciones estarían en archivos aparte, que deben tener una línea al
    # principio que indique si el lenguaje usado es python o el que crearemos,
        # por tanto, ya no pueden depender de funciones en este archivo.

    returned_values = (
        command_handler(argv[index + 1], *argv[index + 2].split("_"))
        for index, command in enumerate(argv)
        if command in {"-c", "--command"} \
        and argv[index + 2] not in {"-c", "--command"}
    )
    return returned_values


def main():
    load_human_language()
    print("\nWelcome to FakeOS!\n")
    command = input(f"{user}@FakeOS$ ")
    command_handler(command)


if __name__ == "__main__":
    main()
