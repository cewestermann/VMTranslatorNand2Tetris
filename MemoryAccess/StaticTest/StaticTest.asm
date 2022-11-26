// push constant 111
@111
D=A
@0
A=M
M=D
// increment StackPointer
@0
M=M+1
// push constant 333
@333
D=A
@0
A=M
M=D
// increment StackPointer
@0
M=M+1
// push constant 888
@888
D=A
@0
A=M
M=D
// increment StackPointer
@0
M=M+1
@258
D=M
@StaticTest.8
M=D
// increment StackPointer
@0
M=M-1
@257
D=M
@StaticTest.3
M=D
// increment StackPointer
@0
M=M-1
@256
D=M
@StaticTest.1
M=D
// increment StackPointer
@0
M=M-1
@StaticTest.3
D=M
@256
M=D
// increment StackPointer
@0
M=M+1
@StaticTest.1
D=M
@257
M=D
// increment StackPointer
@0
M=M+1
// sub
@257
D=M
@256
M=M-D
// increment StackPointer
@0
M=M-1
@StaticTest.8
D=M
@257
M=D
// increment StackPointer
@0
M=M+1
// add
@257
D=M
@256
M=D+M
// increment StackPointer
@0
M=M-1
