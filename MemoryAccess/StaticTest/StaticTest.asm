// push constant 111
@111
D=A
@256
M=D
// increment stack pointer
@SP
M=M+1
// push constant 333
@333
D=A
@257
M=D
// increment stack pointer
@SP
M=M+1
// push constant 888
@888
D=A
@258
M=D
// increment stack pointer
@SP
M=M+1
@SP
A=M-1
D=M
@StaticTest.8
M=D
// decrement stack pointer
@SP
M=M-1
@SP
A=M-1
D=M
@StaticTest.3
M=D
// decrement stack pointer
@SP
M=M-1
@SP
A=M-1
D=M
@StaticTest.1
M=D
// decrement stack pointer
@SP
M=M-1
@StaticTest.3
D=M
@SP
A=M
M=D
// increment stack pointer
@SP
M=M+1
@StaticTest.1
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
@StaticTest.8
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
