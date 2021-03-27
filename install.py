#!/usr/bin/env python3

from os.path import expanduser as get_home
from os.path import join as join_dirs
from os.path import isfile as is_file
from os.path import isdir as is_dir
from setuptools import setup
import configparser
import sys
import os

print("Welcome to FakeOS Installer")


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
        f"cp -f ./main.py {data_dir}",
        f"cp -f ./languages.csv {data_dir}",
        f"cp -f ./translations.cpython*.so {data_dir}",
        f"cp -f -r ./apps {data_dir}",
        f"mv {data_dir}/main.py {data_dir}/FakeOS",
        f"chmod +x {data_dir}/FakeOS",
        f"cp -f ./FakeOS.conf {config_dir}"
    )
    try:
        for command in commands:
            os.system(command)
    except OSError:
        print("An exception occurred during the process.")
        sys.exit(0)
    else:
        print(f'Please add the "{data_dir}" directory to your PATH.')
        print("If you don't know how to do it, visit https://www.cyberciti.biz\
/faq/how-to-add-to-bash-path-permanently-on-linux/")
