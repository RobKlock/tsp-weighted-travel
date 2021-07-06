#!/bin/sh

gcc -o stipple stipple.c rans.c
./stipple
sleep 3
python write-weight-matrix-image.py

echo "done!"
