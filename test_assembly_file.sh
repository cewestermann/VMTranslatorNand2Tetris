#!usr/bin/bash

FILENAME=StaticTest

python -m VMTranslator VMTranslator/$FILENAME.vm

mv ./$FILENAME.asm ./MemoryAccess/$FILENAME/

bash ./tools/CPUEmulator.sh







