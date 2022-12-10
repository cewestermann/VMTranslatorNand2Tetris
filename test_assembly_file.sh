#!usr/bin/bash

FILENAME=PointerTest

python -m VMTranslator VMTranslator/$FILENAME.vm

mv ./$FILENAME.asm ./MemoryAccess/$FILENAME/

bash ./tools/CPUEmulator.sh







