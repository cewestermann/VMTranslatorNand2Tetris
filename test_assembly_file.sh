#!usr/bin/bash

python -m VMTranslator VMTranslator/BasicLoop.vm

mv ./BasicLoop.asm ./ProgramFlow/BasicLoop/

bash ../nand2tetris/tools/CPUEmulator.sh







