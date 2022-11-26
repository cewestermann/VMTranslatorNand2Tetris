#!usr/bin/bash

python -m VMTranslator VMTranslator/StaticTest.vm

mv ./StaticTest.asm ./MemoryAccess/StaticTest/

bash ../nand2tetris/tools/CPUEmulator.sh







