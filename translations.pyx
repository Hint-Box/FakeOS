# Translation module, used to load the languages from the CSV file and print
# messages by giving the code to the show function.

# Note that we use objects instead of strings because C char arrays are
# interpreted as bytes, which gives problems

import urllib
import csv
import sys
import os

cdef class HumanLanguage(object):

    '''Load the contents of the CSV file as a dictionary.'''

    cdef object desired_lang
    cdef object data_path
    cdef object t_file
    cdef object lang_dict
    cdef object lang

    def __init__(self, object desired_lang, object data_path="languages.csv"):

        self.desired_lang = desired_lang
        self.data_path = data_path

        try:
            # We don't use the context manager because it has to be kept open
            # between exception blocks
            self.t_file = open(self.data_path, "r")
        except FileNotFoundError:
            print("Oh no! Couldn't find the CSV translations file, trying to \
download it...")
            try:
                urllib.request.urlretrieve("https://raw.githubusercontent.com\
/Hint-Box/FakeOS/main/languages.csv", data_path)

            except (urllib.error.HTPPError, urllib.error.URLError):
                print(f"Couldn't download the file, please try downloading\
the file from \"https://raw.githubusercontent.com/Hint-Box/FakeOS/main/\
languages.csv\" and save it as {data_path}.")
                self.t_file.close()
                sys.exit(0)

            else:
                print("Done.")

        # If we get here, that means no exceptions occurred

        self.lang_dict = csv.DictReader(self.t_file, delimiter=",")
        for row in self.lang_dict:
            # Search for the specified language in the CSV file
            if bytes(row["Language"], "utf-8") == self.desired_lang:
                self.lang = row
                break
        else:  # Executes only if the loop didn't find the language
            print("Couldn't find the specified language.")
            sys.exit(0)

    cdef object message_id

    cpdef void show(self, object message_id):
        try:
            print(self.lang[message_id])
        except KeyError:
            print(f'Unrecognized message id: "{message_id}"')
