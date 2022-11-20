#!usr/bin/bash

python -m VMTranslator VMTranslator/StackTest.vm

mv ./StackTest.asm ./StackArithmetic/StackTest/

bash ../nand2tetris/tools/CPUEmulator.sh







