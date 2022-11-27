// push constant 17
@17
D=A
@0
A=M
M=D
// increment StackPointer
@0
M=M+1
// push constant 17
@17
D=A
@0
A=M
M=D
// increment StackPointer
@0
M=M+1
// eq
@257
D=M
@256
D=D-M
@eq0
D;JNE// if eq
@256
M=-1
@END_eq0
0;JMP
(eq0)
// if not eq
@256
M=0
(END_eq0)
// increment StackPointer
@0
M=M-1
// push constant 17
@17
D=A
@0
A=M
M=D
// increment StackPointer
@0
M=M+1
// push constant 16
@16
D=A
@0
A=M
M=D
// increment StackPointer
@0
M=M+1
// eq
@258
D=M
@257
D=D-M
@eq1
D;JNE// if eq
@257
M=-1
@END_eq1
0;JMP
(eq1)
// if not eq
@257
M=0
(END_eq1)
// increment StackPointer
@0
M=M-1
// push constant 16
@16
D=A
@0
A=M
M=D
// increment StackPointer
@0
M=M+1
// push constant 17
@17
D=A
@0
A=M
M=D
// increment StackPointer
@0
M=M+1
// eq
@259
D=M
@258
D=D-M
@eq2
D;JNE// if eq
@258
M=-1
@END_eq2
0;JMP
(eq2)
// if not eq
@258
M=0
(END_eq2)
// increment StackPointer
@0
M=M-1
// push constant 892
@892
D=A
@0
A=M
M=D
// increment StackPointer
@0
M=M+1
// push constant 891
@891
D=A
@0
A=M
M=D
// increment StackPointer
@0
M=M+1
// lt
@260
D=M
@259
D=D-M
@lt0
D-1;JLT// if lt
@259
M=-1
@END_lt0
0;JMP
(lt0)
// if not lt
@259
M=0
(END_lt0)
// increment StackPointer
@0
M=M-1
// push constant 891
@891
D=A
@0
A=M
M=D
// increment StackPointer
@0
M=M+1
// push constant 892
@892
D=A
@0
A=M
M=D
// increment StackPointer
@0
M=M+1
// lt
@261
D=M
@260
D=D-M
@lt1
D-1;JLT// if lt
@260
M=-1
@END_lt1
0;JMP
(lt1)
// if not lt
@260
M=0
(END_lt1)
// increment StackPointer
@0
M=M-1
// push constant 891
@891
D=A
@0
A=M
M=D
// increment StackPointer
@0
M=M+1
// push constant 891
@891
D=A
@0
A=M
M=D
// increment StackPointer
@0
M=M+1
// lt
@262
D=M
@261
D=D-M
@lt2
D-1;JLT// if lt
@261
M=-1
@END_lt2
0;JMP
(lt2)
// if not lt
@261
M=0
(END_lt2)
// increment StackPointer
@0
M=M-1
// push constant 32767
@32767
D=A
@0
A=M
M=D
// increment StackPointer
@0
M=M+1
// push constant 32766
@32766
D=A
@0
A=M
M=D
// increment StackPointer
@0
M=M+1
// gt
@263
D=M
@262
D=D-M
@gt0
D+1;JGT// if gt
@262
M=-1
@END_gt0
0;JMP
(gt0)
// if not gt
@262
M=0
(END_gt0)
// increment StackPointer
@0
M=M-1
// push constant 32766
@32766
D=A
@0
A=M
M=D
// increment StackPointer
@0
M=M+1
// push constant 32767
@32767
D=A
@0
A=M
M=D
// increment StackPointer
@0
M=M+1
// gt
@264
D=M
@263
D=D-M
@gt1
D+1;JGT// if gt
@263
M=-1
@END_gt1
0;JMP
(gt1)
// if not gt
@263
M=0
(END_gt1)
// increment StackPointer
@0
M=M-1
// push constant 32766
@32766
D=A
@0
A=M
M=D
// increment StackPointer
@0
M=M+1
// push constant 32766
@32766
D=A
@0
A=M
M=D
// increment StackPointer
@0
M=M+1
// gt
@265
D=M
@264
D=D-M
@gt2
D+1;JGT// if gt
@264
M=-1
@END_gt2
0;JMP
(gt2)
// if not gt
@264
M=0
(END_gt2)
// increment StackPointer
@0
M=M-1
// push constant 57
@57
D=A
@0
A=M
M=D
// increment StackPointer
@0
M=M+1
// push constant 31
@31
D=A
@0
A=M
M=D
// increment StackPointer
@0
M=M+1
// push constant 53
@53
D=A
@0
A=M
M=D
// increment StackPointer
@0
M=M+1
// add
@267
D=M
@266
M=D+M
// increment StackPointer
@0
M=M-1
// push constant 112
@112
D=A
@0
A=M
M=D
// increment StackPointer
@0
M=M+1
// sub
@267
D=M
@266
M=M-D
// increment StackPointer
@0
M=M-1
// neg
@266
M=-M// and
@266
D=M
@265
M=D&M
// increment StackPointer
@0
M=M-1
// push constant 82
@82
D=A
@0
A=M
M=D
// increment StackPointer
@0
M=M+1
// or
@266
D=M
@265
M=D|M
// increment StackPointer
@0
M=M-1
// not
@265
M=!M
