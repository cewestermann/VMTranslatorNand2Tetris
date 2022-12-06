#!usr/bin/bash

FILENAME=FibonacciSeries

python -m VMTranslator VMTranslator/$FILENAME.vm

mv ./$FILENAME.asm ./ProgramFlow/$FILENAME/

bash ./tools/CPUEmulator.sh







