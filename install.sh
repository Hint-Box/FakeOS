#!/bin/bash

echo "Welcome to FakeOS Installer"
DIRECTORY="/home/$USER/.local/FakeOS"

if [ ! -d "$DIRECTORY" ]; then
	echo "Directory doesn't exist, creating..."
	mkdir $DIRECTORY
else
	echo "Directory exists, updating files..."
fi

echo "Copying files..."
cp ./main.py $DIRECTORY
cp ./languages.csv $DIRECTORY
cp ./translations.so $DIRECTORY
cp -r ./apps $DIRECTORY

echo "Preparing file to be executed..."
mv "$DIRECTORY/main.py" "$DIRECTORY/FakeOS"
chmod +x "$DIRECTORY/FakeOS"

echo "Please add the '/home/$USER/.local/FakeOS' directory to your PATH"
echo "If you don't know how to do it, go to https://www.cyberciti.biz/faq/how-to-add-to-bash-path-permanently-on-linux/"

echo "Finished!"