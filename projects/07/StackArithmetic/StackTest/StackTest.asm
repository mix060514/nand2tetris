// push constant 17
@17
D=A
@SP
A=M
M=D
@SP
M=M+1
// push constant 17
@17
D=A
@SP
A=M
M=D
@SP
M=M+1
// eq
@SP
A=M-1
D=M
A=A-1
D=M-D
@If_True_0
D;JEQ
D=0
@End_If_0
1;JMP
(If_True_0)
D=-1
(End_If_0)
@SP
A=M-1
A=A-1
M=D
D=A+1
@SP
M=D
// push constant 17
@17
D=A
@SP
A=M
M=D
@SP
M=M+1
// push constant 16
@16
D=A
@SP
A=M
M=D
@SP
M=M+1
// eq
@SP
A=M-1
D=M
A=A-1
D=M-D
@If_True_1
D;JEQ
D=0
@End_If_1
1;JMP
(If_True_1)
D=-1
(End_If_1)
@SP
A=M-1
A=A-1
M=D
D=A+1
@SP
M=D
// push constant 16
@16
D=A
@SP
A=M
M=D
@SP
M=M+1
// push constant 17
@17
D=A
@SP
A=M
M=D
@SP
M=M+1
// eq
@SP
A=M-1
D=M
A=A-1
D=M-D
@If_True_2
D;JEQ
D=0
@End_If_2
1;JMP
(If_True_2)
D=-1
(End_If_2)
@SP
A=M-1
A=A-1
M=D
D=A+1
@SP
M=D
// push constant 892
@892
D=A
@SP
A=M
M=D
@SP
M=M+1
// push constant 891
@891
D=A
@SP
A=M
M=D
@SP
M=M+1
// lt
@SP
A=M-1
D=M
A=A-1
D=M-D
@If_True_3
D;JLT
D=0
@End_If_3
1;JMP
(If_True_3)
D=-1
(End_If_3)
@SP
A=M-1
A=A-1
M=D
D=A+1
@SP
M=D
// push constant 891
@891
D=A
@SP
A=M
M=D
@SP
M=M+1
// push constant 892
@892
D=A
@SP
A=M
M=D
@SP
M=M+1
// lt
@SP
A=M-1
D=M
A=A-1
D=M-D
@If_True_4
D;JLT
D=0
@End_If_4
1;JMP
(If_True_4)
D=-1
(End_If_4)
@SP
A=M-1
A=A-1
M=D
D=A+1
@SP
M=D
// push constant 891
@891
D=A
@SP
A=M
M=D
@SP
M=M+1
// push constant 891
@891
D=A
@SP
A=M
M=D
@SP
M=M+1
// lt
@SP
A=M-1
D=M
A=A-1
D=M-D
@If_True_5
D;JLT
D=0
@End_If_5
1;JMP
(If_True_5)
D=-1
(End_If_5)
@SP
A=M-1
A=A-1
M=D
D=A+1
@SP
M=D
// push constant 32767
@32767
D=A
@SP
A=M
M=D
@SP
M=M+1
// push constant 32766
@32766
D=A
@SP
A=M
M=D
@SP
M=M+1
// gt
@SP
A=M-1
D=M
A=A-1
D=M-D
@If_True_6
D;JGT
D=0
@End_If_6
1;JMP
(If_True_6)
D=-1
(End_If_6)
@SP
A=M-1
A=A-1
M=D
D=A+1
@SP
M=D
// push constant 32766
@32766
D=A
@SP
A=M
M=D
@SP
M=M+1
// push constant 32767
@32767
D=A
@SP
A=M
M=D
@SP
M=M+1
// gt
@SP
A=M-1
D=M
A=A-1
D=M-D
@If_True_7
D;JGT
D=0
@End_If_7
1;JMP
(If_True_7)
D=-1
(End_If_7)
@SP
A=M-1
A=A-1
M=D
D=A+1
@SP
M=D
// push constant 32766
@32766
D=A
@SP
A=M
M=D
@SP
M=M+1
// push constant 32766
@32766
D=A
@SP
A=M
M=D
@SP
M=M+1
// gt
@SP
A=M-1
D=M
A=A-1
D=M-D
@If_True_8
D;JGT
D=0
@End_If_8
1;JMP
(If_True_8)
D=-1
(End_If_8)
@SP
A=M-1
A=A-1
M=D
D=A+1
@SP
M=D
// push constant 57
@57
D=A
@SP
A=M
M=D
@SP
M=M+1
// push constant 31
@31
D=A
@SP
A=M
M=D
@SP
M=M+1
// push constant 53
@53
D=A
@SP
A=M
M=D
@SP
M=M+1
// add
@SP
A=M-1
D=M
A=A-1
M=M+D
D=A+1
@SP
M=D
// push constant 112
@112
D=A
@SP
A=M
M=D
@SP
M=M+1
// sub
@SP
A=M-1
D=M
A=A-1
M=M-D
D=A+1
@SP
M=D
// neg
@SP
A=M-1
M=-M
// and
@SP
A=M-1
D=M
A=A-1
M=M&D
D=A+1
@SP
M=D
// push constant 82
@82
D=A
@SP
A=M
M=D
@SP
M=M+1
// or
@SP
A=M-1
D=M
A=A-1
M=M|D
D=A+1
@SP
M=D
// not
@SP
A=M-1
M=!M
