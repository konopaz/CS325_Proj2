#!/bin/bash
echo "packing up deliverables into zip file..."

rm -Rf Group24Project2.zip
rm -Rf Group24Project2

mkdir -p Group24Project2
cp README.md Group24Project2/
cp change.py Group24Project2/
cp benchmark.py Group24Project2/
cp testchange.py Group24Project2/
cp package.sh Group24Project2/

zip -r Group24Project2.zip Group24Project2

rm -Rf Group24Project2
