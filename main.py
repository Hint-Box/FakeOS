#!/usr/bin/python

import sys  # Will be widely used in all the program
import os

import csv  # Used for translation system
import urllib.request  # Used for downloading data

from os.path import join as join_dirs
from os.path import isfile as is_file
from os.path import isdir as is_dir
from getpass import getuser  # Used to obtain the username for the shell


user = getuser()

command_dict = {
    "s": "s"
}

data_path = join_dirs(os.path.expanduser("~"), ".local", "FakeOS")
languages_path = join_dirs(data_path, "languages.csv")

# Code for translation system
class LoadHumanLanguage:
    # The initialization of this class tries to find the csv file with translations
    def __init__(self):
        if not is_dir(data_path):
            try:
                os.makedirs(data_path)
            except OSError as id:
                print(f"Oh, no! An exception occurred. Details: {id}")

        if not is_file(languages_path):
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
    def get_string(self, language, str_id):
        with open(languages_path, "r") as t_file:
            langs = csv.DictReader(t_file, delimiter=",")
            for row in langs:
                # Search for specified language in the csv file
                if row["Language"] == language:
                    # If the specified language is found, return the requested string after checking it exists
                    if str_id in row:
                        return row[str_id]
                    # If requested string doesn't exist, return an error
                    return "String not found!"
            # If requested language doesn't exist, return an error
            return "Language not found!"
        

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
    l = LoadHumanLanguage()
    # print(l.get_string("Esperanto", "welcome_msg"))
    print("\nWelcome to FakeOS!\n")
    command = input(f"{user}@FakeOS$ ")
    command_handler(command)


if __name__ == "__main__":
    main()
