// push constant 10
@10
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
// push constant 21
@21
D=A
@256
M=D
// increment stack pointer
@SP
M=M+1
// push constant 22
@22
D=A
@257
M=D
// increment stack pointer
@SP
M=M+1
// pop ARG 2
// Store offset in Register 13
@2
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
// pop ARG 1
// Store offset in Register 13
@1
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
// push constant 36
@36
D=A
@256
M=D
// increment stack pointer
@SP
M=M+1
// pop THIS 6
// Store offset in Register 13
@6
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
// push constant 42
@42
D=A
@256
M=D
// increment stack pointer
@SP
M=M+1
// push constant 45
@45
D=A
@257
M=D
// increment stack pointer
@SP
M=M+1
// pop THAT 5
// Store offset in Register 13
@5
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
// push constant 510
@510
D=A
@256
M=D
// increment stack pointer
@SP
M=M+1
// pop temp 6
@256
D=M
@11
M=D
// decrement stack pointer
@SP
M=M-1
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
// push THAT 5
@5
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
// push THIS 6
@6
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
// push THIS 6
@6
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
// push temp 6
@11
D=M
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
