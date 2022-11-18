// push constant 17
@17
D=A
@0
A=M
M=D
// increment stack pointer
@0
M=M+1
// push constant 17
@17
D=A
@0
A=M
M=D
// increment stack pointer
@0
M=M+1
// eq
@257
D=M
@256
D=D-M
@EQ0
D;JNE
// if equal:
@256
M=-1
(EQ0)
// if not equal
@256
M=1
// push constant 17
@17
D=A
@0
A=M
M=D
// increment stack pointer
@0
M=M+1
// push constant 16
@16
D=A
@0
A=M
M=D
// increment stack pointer
@0
M=M+1
// eq
@258
D=M
@257
D=D-M
@EQ1
D;JNE
// if equal:
@257
M=-1
(EQ1)
// if not equal
@257
M=1
// push constant 16
@16
D=A
@0
A=M
M=D
// increment stack pointer
@0
M=M+1
// push constant 17
@17
D=A
@0
A=M
M=D
// increment stack pointer
@0
M=M+1
// eq
@259
D=M
@258
D=D-M
@EQ2
D;JNE
// if equal:
@258
M=-1
(EQ2)
// if not equal
@258
M=1
// push constant 892
@892
D=A
@0
A=M
M=D
// increment stack pointer
@0
M=M+1
// push constant 891
@891
D=A
@0
A=M
M=D
// increment stack pointer
@0
M=M+1
