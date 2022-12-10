#!usr/bin/bash

FILENAME=BasicTest

python -m VMTranslator VMTranslator/$FILENAME.vm

mv ./$FILENAME.asm ./MemoryAccess/$FILENAME/

bash ./tools/CPUEmulator.sh







