# Translation module, used to load the languages from the CSV file and print
# messages by giving the code to the show function.

# Note that we use objects instead of strings when using them as indexes
# because C char arrays are interpreted as bytes, which gives problems

# Variables that need to be used as arguments for Python standard functions are
# created as generic objects, regardless of their availability in the C library.
# For example: File Objects
# This rule CAN apply to 3rd party libraries too.

import urllib.request
import urllib.error
from sys import exit
import csv


cdef class HumanLanguage:

    '''Load the contents of the CSV file as a dictionary.'''

    cdef char* desired_lang
    cdef char* data_path
    cdef object t_file  # File Object
    cdef object lang_dict  # csv.DictReader
    cdef dict lang
    cdef dict row

    cdef object message_id  # String


    def __init__(self, char* desired_lang, char* data_path=b"languages.csv"):

        self.desired_lang = desired_lang
        self.data_path = data_path

        try:
            self.t_file = open(self.data_path, "r")
        except FileNotFoundError:
            print("Oh no! Couldn't find the CSV translations file, trying to \
download it...")
            try:
                urllib.request.urlretrieve("https://raw.githubusercontent.com\
/Hint-Box/FakeOS/main/languages.csv", data_path)

            except (urllib.error.HTPPError, urllib.error.URLError):
                print(f'Failed, please try downloading the file from "https:/\
/raw.githubusercontent.com/Hint-Box/FakeOS/main/languages.csv" and save it as\
{data_path}.')
                exit(0)

            else:
                self.t_file = open(self.data_path, "r")
                print("Done.")

        # If we get here, that means urllib didn't raise an exception

        self.lang_dict = csv.DictReader(self.t_file, delimiter=",")
        for row in self.lang_dict:
            # Search for the specified language in the CSV file
            if bytes(row["Language"], "utf-8") == self.desired_lang:
                self.lang = row.copy()
                self.t_file.close()
                break
        else:  # Executes only if the loop didn't find the language

            # The user is not supposed to experience this, this constructor
            # can only get valid arguments. For more information see the
            # main.py file.

            print("ERROR: Couldn't find the specified language.")
            self.t_file.close()
            exit(0)

    cpdef object get(self, object message_id):  # String
        try:
            return self.lang[message_id]
        except KeyError:
            #print(f'Unrecognized message id: "{message_id}"')
            return ""
