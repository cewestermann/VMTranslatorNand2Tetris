#!usr/bin/bash

python -m VMTranslator VMTranslator/PointerTest.vm

mv ./PointerTest.asm ./MemoryAccess/PointerTest/

bash ../nand2tetris/tools/CPUEmulator.sh







