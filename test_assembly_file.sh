#!usr/bin/bash

FILENAME=StackTest

python -m VMTranslator VMTranslator/$FILENAME.vm

mv ./$FILENAME.asm ./StackArithmetic/$FILENAME/

bash ./tools/CPUEmulator.sh







