// push argument 1
@401
D=M
@256
M=D
// increment stack pointer
@0
M=M+1
// pop pointer 1
@256
D=M
@4
M=D
// decrement stack pointer
@0
M=M-1
// push constant 0
@0
D=A
@256
M=D
// increment stack pointer
@0
M=M+1
// pop that 0
@256
D=M
@3010
M=D
// decrement stack pointer
@0
M=M-1
// push constant 1
@1
D=A
@256
M=D
// increment stack pointer
@0
M=M+1
// pop that 1
@256
D=M
@3011
M=D
// decrement stack pointer
@0
M=M-1
// push argument 0
@400
D=M
@256
M=D
// increment stack pointer
@0
M=M+1
// push constant 2
@2
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
@256
D=M
@400
M=D
// decrement stack pointer
@0
M=M-1
(global$MAIN_LOOP_START)
// push argument 0
@400
D=M
@256
M=D
// increment stack pointer
@0
M=M+1
// if-goto COMPUTE_ELEMENT
@256
D=M
// decrement stack pointer
@0
M=M-1
@global$COMPUTE_ELEMENT
D;JNE
// goto END_PROGRAM
@END_PROGRAM
0;JMP
(global$COMPUTE_ELEMENT)
// push that 0
@3010
D=M
@256
M=D
// increment stack pointer
@0
M=M+1
// push that 1
@3011
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
// pop that 2
@256
D=M
@3012
M=D
// decrement stack pointer
@0
M=M-1
// push pointer 1
@4
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
// add
@257
D=M
@256
M=D+M
// decrement stack pointer
@0
M=M-1
// pop pointer 1
@256
D=M
@4
M=D
// decrement stack pointer
@0
M=M-1
// push argument 0
@400
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
@256
D=M
@400
M=D
// decrement stack pointer
@0
M=M-1
// goto MAIN_LOOP_START
@MAIN_LOOP_START
0;JMP
(global$END_PROGRAM)
