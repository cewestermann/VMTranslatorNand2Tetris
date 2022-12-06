// push constant 0
@0
D=A
@256
M=D
// increment stack pointer
@0
M=M+1
// pop local 0
@0
D=A
@1
D=D+M
@MemorySegment1
M=D
@256
D=M
@MemorySegment1
A=M
M=D
// decrement stack pointer
@0
M=M-1
(global$LOOP_START)
// push argument 0
@0
D=A
@2
A=D+M
D=M
@256
M=D
// increment stack pointer
@0
M=M+1
// push local 0
@0
D=A
@1
A=D+M
D=M
@257
M=D
// increment stack pointer
@0
M=M+1
// add
@257
D=M
@256
M=D+M
// decrement stack pointer
@0
M=M-1
// pop local 0
@0
D=A
@1
D=D+M
@MemorySegment3
M=D
@256
D=M
@MemorySegment3
A=M
M=D
// decrement stack pointer
@0
M=M-1
// push argument 0
@0
D=A
@2
A=D+M
D=M
@256
M=D
// increment stack pointer
@0
M=M+1
// push constant 1
@1
D=A
@257
M=D
// increment stack pointer
@0
M=M+1
// sub
@257
D=M
@256
M=M-D
// decrement stack pointer
@0
M=M-1
// pop argument 0
@0
D=A
@2
D=D+M
@MemorySegment3
M=D
@256
D=M
@MemorySegment3
A=M
M=D
// decrement stack pointer
@0
M=M-1
// push argument 0
@0
D=A
@2
A=D+M
D=M
@256
M=D
// increment stack pointer
@0
M=M+1
// if-goto LOOP_START
@256
D=M
// decrement stack pointer
@0
M=M-1
@global$LOOP_START
D;JNE
// push local 0
@0
D=A
@1
A=D+M
D=M
@256
M=D
// increment stack pointer
@0
M=M+1
