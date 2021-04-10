# Translation module, used to load the idioms from the CSV file and print
# messages by giving the message identifier to the show function.

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

# Note that we use Python objects instead of strings when using them as indexes
# because C character arrays are interpreted as bytes, which gives problems

# Variables that need to be used as arguments for Python standard functions are
# created as generic objects, regardless of their availability in the C library
# This rule applies to third party libraries too unless they have an explicit C
# type declaration file (PYXD), like NumPy.

# cython: language_level=3

import urllib.request
import urllib.error
from sys import exit
import csv


cdef class Idiom:
    """Load the contents of the CSV file as a Python nested dictionary."""

    # Variables used in the constructor
    cdef char* desired_idiom
    cdef char* data_path
    cdef object t_file  # File object
    cdef object idiom_dict  # csv.DictReader object
    cdef dict idiom
    cdef dict row

    # Variable used in the get method
    cdef object msg_id  # String


    def __init__(self, char* desired_idiom, char* data_path=b"idioms.csv"):

        self.desired_idiom = desired_idiom
        self.data_path = data_path

        try:
            self.t_file = open(self.data_path, "r")
        except FileNotFoundError:
            print("Oh no! Couldn't find the CSV translations file, trying to \
download it...")
            try:
                urllib.request.urlretrieve("https://raw.githubusercontent.com\
/Hint-Box/FakeOS/main/idioms.csv", self.data_path)

            except urllib.error.URLError:
                print(f'Failed, please try downloading the file from "https:/\
/raw.githubusercontent.com/Hint-Box/FakeOS/main/idioms.csv" and save it as\
{data_path}.')
                # WiP: Define a dictionary here with the basic messages
                # self.idiom = self.basic_english.copy()
            else:
                print("Done.")
        else:
            with self.t_file:
                self.idiom_dict = csv.DictReader(self.t_file, delimiter=",")

                # Search for the specified idiom in the CSV file
                for row in self.idiom_dict:
                    if bytes(row["Idiom"], "utf-8") == self.desired_idiom:
                        self.idiom = row.copy()
                        break
                else:
                    # The user is not supposed to experience this, as the
                    # constructor can only get previously validated values.

                    print("ERROR: Couldn't find the specified idiom.")
                    exit(0)

    cpdef object get(self, object msg_id):
        """Returns the message in self.idiom with the specified ID."""
        try:
            return self.idiom[msg_id]
        except KeyError:
            return ""  # Allows the basic messages thing
