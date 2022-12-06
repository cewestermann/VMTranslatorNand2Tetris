#!usr/bin/bash

FILENAME=BasicLoop

python -m VMTranslator VMTranslator/$FILENAME.vm

mv ./$FILENAME.asm ./ProgramFlow/$FILENAME/

bash ./tools/CPUEmulator.sh







