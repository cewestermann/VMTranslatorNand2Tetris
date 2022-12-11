// push ARG 1
@1
D=A
@ARG
A=M+D
D=M
@SP
A=M
M=D
// increment stack pointer
@SP
M=M+1
// pop PNTR 1
// Store offset in Register 13
@1
D=A
@3
D=A+D
@R13
M=D
// Save Stack value and use Register 13 to pop to segment
@SP
A=M-1
D=M
@R13
A=M
M=D
// decrement stack pointer
@SP
M=M-1
// push constant 0
@0
D=A
@256
M=D
// increment stack pointer
@SP
M=M+1
// pop THAT 0
// Store offset in Register 13
@0
D=A
@THAT
D=M+D
@R13
M=D
// Save Stack value and use Register 13 to pop to segment
@SP
A=M-1
D=M
@R13
A=M
M=D
// decrement stack pointer
@SP
M=M-1
// push constant 1
@1
D=A
@256
M=D
// increment stack pointer
@SP
M=M+1
// pop THAT 1
// Store offset in Register 13
@1
D=A
@THAT
D=M+D
@R13
M=D
// Save Stack value and use Register 13 to pop to segment
@SP
A=M-1
D=M
@R13
A=M
M=D
// decrement stack pointer
@SP
M=M-1
// push ARG 0
@0
D=A
@ARG
A=M+D
D=M
@SP
A=M
M=D
// increment stack pointer
@SP
M=M+1
// push constant 2
@2
D=A
@257
M=D
// increment stack pointer
@SP
M=M+1
// sub
@SP
A=M-1
D=M
@SP
A=M-1
A=A-1
M=M-D
// decrement stack pointer
@SP
M=M-1
// pop ARG 0
// Store offset in Register 13
@0
D=A
@ARG
D=M+D
@R13
M=D
// Save Stack value and use Register 13 to pop to segment
@SP
A=M-1
D=M
@R13
A=M
M=D
// decrement stack pointer
@SP
M=M-1
(global$MAIN_LOOP_START)
// push ARG 0
@0
D=A
@ARG
A=M+D
D=M
@SP
A=M
M=D
// increment stack pointer
@SP
M=M+1
// if-goto COMPUTE_ELEMENT
@256
D=M
// decrement stack pointer
@SP
M=M-1
@global$COMPUTE_ELEMENT
D;JNE
// goto END_PROGRAM
@END_PROGRAM
0;JMP
(global$COMPUTE_ELEMENT)
// push THAT 0
@0
D=A
@THAT
A=M+D
D=M
@SP
A=M
M=D
// increment stack pointer
@SP
M=M+1
// push THAT 1
@1
D=A
@THAT
A=M+D
D=M
@SP
A=M
M=D
// increment stack pointer
@SP
M=M+1
// add
@SP
A=M-1
D=M
@SP
A=M-1
A=A-1
M=D+M
// decrement stack pointer
@SP
M=M-1
// pop THAT 2
// Store offset in Register 13
@2
D=A
@THAT
D=M+D
@R13
M=D
// Save Stack value and use Register 13 to pop to segment
@SP
A=M-1
D=M
@R13
A=M
M=D
// decrement stack pointer
@SP
M=M-1
// push PNTR 1
@1
D=A
@3
A=A+D
D=M
@SP
A=M
M=D
// increment stack pointer
@SP
M=M+1
// push constant 1
@1
D=A
@257
M=D
// increment stack pointer
@SP
M=M+1
// add
@SP
A=M-1
D=M
@SP
A=M-1
A=A-1
M=D+M
// decrement stack pointer
@SP
M=M-1
// pop PNTR 1
// Store offset in Register 13
@1
D=A
@3
D=A+D
@R13
M=D
// Save Stack value and use Register 13 to pop to segment
@SP
A=M-1
D=M
@R13
A=M
M=D
// decrement stack pointer
@SP
M=M-1
// push ARG 0
@0
D=A
@ARG
A=M+D
D=M
@SP
A=M
M=D
// increment stack pointer
@SP
M=M+1
// push constant 1
@1
D=A
@257
M=D
// increment stack pointer
@SP
M=M+1
// sub
@SP
A=M-1
D=M
@SP
A=M-1
A=A-1
M=M-D
// decrement stack pointer
@SP
M=M-1
// pop ARG 0
// Store offset in Register 13
@0
D=A
@ARG
D=M+D
@R13
M=D
// Save Stack value and use Register 13 to pop to segment
@SP
A=M-1
D=M
@R13
A=M
M=D
// decrement stack pointer
@SP
M=M-1
// goto MAIN_LOOP_START
@MAIN_LOOP_START
0;JMP
(global$END_PROGRAM)
