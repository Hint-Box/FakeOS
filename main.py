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


user = getuser()


data_path = join_dirs(os.path.expanduser("~"), ".local", "FakeOS")
languages_path = join_dirs(data_path, "languages.csv")

# Code for translation system
class LoadHumanLanguage:
    # The initialization of this class tries to find the csv file with translations
    def __init__(self, language):
        self.language = language
        if not is_dir(data_path) and not is_file("languages.csv"):
            try:
                os.makedirs(data_path)
            except OSError as id:
                print(f"Oh, no! An exception occurred. Details: {id}")

        if not is_file(languages_path) and not is_file("languages.csv"):
            print("Oh, no! We cannot find the CSV file for other languages, trying to download it...")

            try:
                urllib.request.urlretrieve("https://raw.githubusercontent.com/Hint-Box/FakeOS/main/languages.csv",languages_path)
                print("Downloaded!")

            except Exception as id:
                print(f"Oops, we had an error while getting the file, please try\
    downloading \"https://raw.githubusercontent.com/Hint-Box/FakeOS/main/\
    languages.csv\" manually, then save it to {data_path}.")
                print(f"Details: {id}")

    # This function is used to obtain the translations from the csv file
    def get_string(self, str_id):
        try:
            with open(languages_path, "r") as t_file:
                langs = csv.DictReader(t_file, delimiter=",")
                for row in langs:
                    # Search for specified language in the csv file
                    if row["Language"] == self.language:
                        # If the specified language is found, return the requested string after checking it exists
                        if str_id in row:
                            return row[str_id]
                        # If requested string doesn't exist, return an error
                        return "String not found!"
                # If requested language doesn't exist, return an error
                return "Language not found!"
        except FileNotFoundError:
            with open("languages.csv", "r") as t_file:
                langs = csv.DictReader(t_file, delimiter=",")
                for row in langs:
                    # Search for specified language in the csv file
                    if row["Language"] == self.language:
                        # If the specified language is found, return the requested string after checking it exists
                        if str_id in row:
                            return row[str_id]
                        # If requested string doesn't exist, return an error
                        return "String not found!"
                # If requested language doesn't exist, return an error
                return "Language not found!"


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
    # Detect default language and initialize LoadHumanLanguage class with it
    loc = locale.getdefaultlocale()[0]
    if loc.startswith("en"):
        l = LoadHumanLanguage("English")
    elif loc.startswith("es"):
        l = LoadHumanLanguage("Spanish")
    elif loc.startswith("eo"):
            l = LoadHumanLanguage("Esperanto")
    
    print(f"\n{l.get_string('welcome_msg')}\n")
    
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
