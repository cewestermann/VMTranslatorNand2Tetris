// push constant 3030
@3030
D=A
@256
M=D
// increment stack pointer
@SP
M=M+1
// pop PNTR 0
// Store offset in Register 13
@0
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
// push constant 3040
@3040
D=A
@256
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
// push constant 32
@32
D=A
@256
M=D
// increment stack pointer
@SP
M=M+1
// pop THIS 2
// Store offset in Register 13
@2
D=A
@THIS
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
// push constant 46
@46
D=A
@256
M=D
// increment stack pointer
@SP
M=M+1
// pop THAT 6
// Store offset in Register 13
@6
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
// push PNTR 0
@0
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
// push THIS 2
@2
D=A
@THIS
A=M+D
D=M
@SP
A=M
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
// push THAT 6
@6
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
