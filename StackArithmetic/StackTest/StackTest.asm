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
// EQ
@257
D=M
@256
D=D-M
@EQ0
D;JNE
// if EQ
@256
M=-1
@END_EQ0
0;JMP
(EQ0)
// if not EQ
@256
M=0
(END_EQ0)
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
// EQ
@258
D=M
@257
D=D-M
@EQ1
D;JNE
// if EQ
@257
M=-1
@END_EQ1
0;JMP
(EQ1)
// if not EQ
@257
M=0
(END_EQ1)
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
// EQ
@259
D=M
@258
D=D-M
@EQ2
D;JNE
// if EQ
@258
M=-1
@END_EQ2
0;JMP
(EQ2)
// if not EQ
@258
M=0
(END_EQ2)
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
// LT
@260
D=M
@259
D=D-M
@LT0
D;JGT
// if LT
@259
M=-1
@END_LT0
0;JMP
(LT0)
// if not LT
@259
M=0
(END_LT0)
// push constant 891
@891
D=A
@0
A=M
M=D
// increment stack pointer
@0
M=M+1
// push constant 892
@892
D=A
@0
A=M
M=D
// increment stack pointer
@0
M=M+1
// LT
@261
D=M
@260
D=D-M
@LT1
D;JGT
// if LT
@260
M=-1
@END_LT1
0;JMP
(LT1)
// if not LT
@260
M=0
(END_LT1)
// push constant 891
@891
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
// LT
@262
D=M
@261
D=D-M
@LT2
D;JGT
// if LT
@261
M=-1
@END_LT2
0;JMP
(LT2)
// if not LT
@261
M=0
(END_LT2)
// push constant 32767
@32767
D=A
@0
A=M
M=D
// increment stack pointer
@0
M=M+1
// push constant 32766
@32766
D=A
@0
A=M
M=D
// increment stack pointer
@0
M=M+1
// GT
@263
D=M
@262
D=D-M
@GT0
D;JLT
// if GT
@262
M=-1
@END_GT0
0;JMP
(GT0)
// if not GT
@262
M=0
(END_GT0)
// push constant 32766
@32766
D=A
@0
A=M
M=D
// increment stack pointer
@0
M=M+1
// push constant 32767
@32767
D=A
@0
A=M
M=D
// increment stack pointer
@0
M=M+1
// GT
@264
D=M
@263
D=D-M
@GT1
D;JLT
// if GT
@263
M=-1
@END_GT1
0;JMP
(GT1)
// if not GT
@263
M=0
(END_GT1)
// push constant 32766
@32766
D=A
@0
A=M
M=D
// increment stack pointer
@0
M=M+1
// push constant 32766
@32766
D=A
@0
A=M
M=D
// increment stack pointer
@0
M=M+1
// GT
@265
D=M
@264
D=D-M
@GT2
D;JLT
// if GT
@264
M=-1
@END_GT2
0;JMP
(GT2)
// if not GT
@264
M=0
(END_GT2)
// push constant 57
@57
D=A
@0
A=M
M=D
// increment stack pointer
@0
M=M+1
// push constant 31
@31
D=A
@0
A=M
M=D
// increment stack pointer
@0
M=M+1
// push constant 53
@53
D=A
@0
A=M
M=D
// increment stack pointer
@0
M=M+1
// add
@267
D=M
@266
M=D+M
// decrement stack pointer
@0
M=M-1
// push constant 112
@112
D=A
@0
A=M
M=D
// increment stack pointer
@0
M=M+1
// sub
@267
D=M
@266
M=D-M
// decrement stack pointer
@0
M=M-1
// neg
@266
M=-M