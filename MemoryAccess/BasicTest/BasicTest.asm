// push constant 10
@10
D=A
@0
A=M
M=D
// increment StackPointer
@0
M=M+1
// pop local 0
@0
D=M
@1
D=D+M
@Segment1
M=D
@256
D=M
@Segment1
A=M
M=D
// increment StackPointer
@0
M=M-1
// push constant 21
@21
D=A
@0
A=M
M=D
// increment StackPointer
@0
M=M+1
// push constant 22
@22
D=A
@0
A=M
M=D
// increment StackPointer
@0
M=M+1
// pop argument 2
@2
D=M
@2
D=D+M
@Segment1
M=D
@257
D=M
@Segment1
A=M
M=D
// increment StackPointer
@0
M=M-1
// pop argument 1
@1
D=M
@2
D=D+M
@Segment2
M=D
@256
D=M
@Segment2
A=M
M=D
// increment StackPointer
@0
M=M-1
// push constant 36
@36
D=A
@0
A=M
M=D
// increment StackPointer
@0
M=M+1
// pop this 6
@6
D=M
@3
D=D+M
@Segment1
M=D
@256
D=M
@Segment1
A=M
M=D
// increment StackPointer
@0
M=M-1
// push constant 42
@42
D=A
@0
A=M
M=D
// increment StackPointer
@0
M=M+1
// push constant 45
@45
D=A
@0
A=M
M=D
// increment StackPointer
@0
M=M+1
// pop that 5
@5
D=M
@4
D=D+M
@Segment1
M=D
@257
D=M
@Segment1
A=M
M=D
// increment StackPointer
@0
M=M-1
// pop that 2
@2
D=M
@4
D=D+M
@Segment2
M=D
@256
D=M
@Segment2
A=M
M=D
// increment StackPointer
@0
M=M-1
// push constant 510
@510
D=A
@0
A=M
M=D
// increment StackPointer
@0
M=M+1
// pop temp 6
@6
D=M
@5
D=D+M
@Segment1
M=D
@256
D=M
@Segment1
A=M
M=D
// increment StackPointer
@0
M=M-1
// push local 0
@0
D=M
@1
D=D+M
@Segment2
M=D
@256
D=M
@Segment2
A=M
M=D
// increment StackPointer
@0
M=M+1
// push that 5
@5
D=M
@4
D=D+M
@Segment3
M=D
@257
D=M
@Segment3
A=M
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
// push argument 1
@1
D=M
@2
D=D+M
@Segment3
M=D
@257
D=M
@Segment3
A=M
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
// push this 6
@6
D=M
@3
D=D+M
@Segment2
M=D
@257
D=M
@Segment2
A=M
M=D
// increment StackPointer
@0
M=M+1
// push this 6
@6
D=M
@3
D=D+M
@Segment3
M=D
@258
D=M
@Segment3
A=M
M=D
// increment StackPointer
@0
M=M+1
// add
@258
D=M
@257
M=D+M
// increment StackPointer
@0
M=M-1
// sub
@257
D=M
@256
M=M-D
// increment StackPointer
@0
M=M-1
// push temp 6
@6
D=M
@5
D=D+M
@Segment2
M=D
@257
D=M
@Segment2
A=M
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
