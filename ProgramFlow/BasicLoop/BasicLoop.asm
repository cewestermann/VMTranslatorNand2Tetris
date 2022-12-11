// push constant 0
@0
D=A
@256
M=D
// increment stack pointer
@SP
M=M+1
// pop LCL 0
// Store offset in Register 13
@0
D=A
@LCL
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
(global$LOOP_START)
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
// push LCL 0
@0
D=A
@LCL
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
// pop LCL 0
// Store offset in Register 13
@0
D=A
@LCL
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
// if-goto LOOP_START
@256
D=M
// decrement stack pointer
@SP
M=M-1
@global$LOOP_START
D;JNE
// push LCL 0
@0
D=A
@LCL
A=M+D
D=M
@SP
A=M
M=D
// increment stack pointer
@SP
M=M+1
