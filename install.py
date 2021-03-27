#!/usr/bin/env python3
import os, configparser # Used to execute system functions and to configure the program
import sys
from getpass import getuser # To get the username
from setuptools import setup # Used to compile Cython code

print("Welcome to FakeOS Installer")

user = getuser()
data_path = f"/home/{user}/.local/FakeOS/"
config_path = f"/home/{user}/.config/FakeOS"

print("Checking if data folder exists...")
if not os.path.exists(data_path):
    print("Data folder doesn't exist, creating...")
    os.makedirs(data_path)
else:
    print("Data folder exists, updating content...")

print("Checking if config folder exists...")
if not os.path.exists(config_path):
    print("Config folder doesn't exist, creating...")
    os.makedirs(config_path)
else:
    print("Config folder exists, updating content...")

print("Building translations.pyx with Cython")
plt = sys.platform
if plt.startswith("linux") or plt.startswith("darwin"):
    try:
        os.system("python3 setup.py build_ext --inplace")
    except:
        print("We cannot build the file")
        sys.exit()
elif plt.startswith("win"):
    print("Your platform is not currently supported!")
    sys.exit()
else:
    print("We cannot determine your platform!")
    sys.exit()

print("Copying files...")
try:
    if plt.startswith("linux") or plt.startswith(darwin):
        commands = [f"cp -f ./main.py {data_path}", \
                    f"cp -f ./languages.csv {data_path}", \
                    f"cp -f ./translations.cpython*.so {data_path}", \
                    f"cp -f -r ./apps {data_path}", \
                    f"mv {data_path}/main.py {data_path}/FakeOS", \
                    f"chmod +x {data_path}/FakeOS", \
                    f"cp -f ./FakeOS.conf {config_path}"]
        for command in commands:
            os.system(command)
        print(f"Please add the '/home/{user}/.local/FakeOS' directory to your PATH")
        print(f"If you don't know how to do it, go to https://www.cyberciti.biz/faq/how-to-add-to-bash-path-permanently-on-linux/")

except Exception as e:
    print("Error:", e)
    sys.exit()
