#!usr/bin/bash

python -m VMTranslator VMTranslator/BasicTest.vm

mv ./BasicTest.asm ./MemoryAccess/BasicTest/

bash ../nand2tetris/tools/CPUEmulator.sh







