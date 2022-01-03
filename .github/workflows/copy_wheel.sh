#! /bin/bash

echo "$(pwd)"

#Locate the universal wheel file
file=$(find ./dist -type f -name "*py2.py3*.whl") 

#Check if has found the universal wheel
if [ "$file" = "" ]; then
  echo "Universal wheel not found!"
  exit 0
fi

#Copy the cp37 version
cp "$file" "${file//py2.py3-none/cp37-cp37}"

#Copy the cp38 version
cp "$file" "${file//py2.py3-none/cp38-cp38}"

#Copy the cp39 version
cp "$file" "${file//py2.py3-none/cp39-cp39}"

#Remove the universal wheel
rm "$file"
