#!/usr/bin/env python3

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

from os.path import expanduser as get_home
from os.path import join as join_dirs
from os.path import isdir as is_dir
# import configparser
import sys
import os

print("\nWelcome to the FakeOS Installer\n")


def install_fakeos():

    home_path = get_home("~")
    data_dir = join_dirs(home_path, ".local/FakeOS")
    config_dir = join_dirs(home_path, ".config/FakeOS")

    print("Checking if data directory exists...")
    if is_dir(data_dir):
        print("Data directory exists, updating content...")
    else:
        print("Data directory doesn't exist, creating it...")

    print("Checking if config directory exists...")
    if is_dir(config_dir):
        print("Config directory doesn't exist, creating it...")
        os.makedirs(config_dir)
    else:
        print("Config directory exists, updating content...")

    print("Building translations.pyx with Cython...")
    if sys.platform[:5] == "linux" or sys.platform[:6] == "darwin":
        try:
            os.system("python3 setup.py build_ext --inplace")
        except OSError:
            print("An exception occurred during the building process.")
            sys.exit(0)
    else:
        print("Your platform is not currently supported!")
        sys.exit(0)

    print("Copying files...")
    commands = (
        f"cp -fv main.py {data_dir}",
        f"cp -fv languages.csv {data_dir}",
        f"cp -fv translations.*.so {data_dir}",
        f"cp -fvr apps {data_dir}",
        f"mv {data_dir}/main.py {data_dir}/FakeOS",
        f"chmod +x {data_dir}/FakeOS",
        f"cp -fv FakeOS.conf {config_dir}"
    )
    try:
        for command in commands:
            os.system(command)
    except OSError:
        print("An exception occurred during the process.")
        sys.exit(0)
    else:
        print(f'Please add the "{data_dir}" directory to your PATH.')
        print('If you don"t know how to do it, visit "https://www.cyberciti.biz\
/faq/how-to-add-to-bash-path-permanently-on-linux/"')
