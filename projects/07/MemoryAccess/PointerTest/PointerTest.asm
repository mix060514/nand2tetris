// push constant 3030
@3030
D=A
@SP
A=M
M=D
@SP
M=M+1
// pop pointer 0
@SP
A=M-1
D=M
@THIS
M=D
@SP
M=M-1
// push constant 3040
@3040
D=A
@SP
A=M
M=D
@SP
M=M+1
// pop pointer 1
@SP
A=M-1
D=M
@THAT
M=D
@SP
M=M-1
// push constant 32
@32
D=A
@SP
A=M
M=D
@SP
M=M+1
// pop this 2
@2
D=A
@THIS
M=M+D
@SP
M=M-1
A=M
D=M
@THIS
A=M
M=D
@2
D=A
@THIS
M=M-D
// push constant 46
@46
D=A
@SP
A=M
M=D
@SP
M=M+1
// pop that 6
@6
D=A
@THAT
M=M+D
@SP
M=M-1
A=M
D=M
@THAT
A=M
M=D
@6
D=A
@THAT
M=M-D
// push pointer 0
@THIS
D=M
@SP
A=M
M=D
@SP
M=M+1
// push pointer 1
@THAT
D=M
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
// push this 2
@2
D=A
@THIS
M=M+D
A=M
D=M
@SP
A=M
M=D
@SP
M=M+1
@2
D=A
@THIS
M=M-D
// sub
@SP
A=M-1
D=M
A=A-1
M=M-D
D=A+1
@SP
M=D
// push that 6
@6
D=A
@THAT
M=M+D
A=M
D=M
@SP
A=M
M=D
@SP
M=M+1
@6
D=A
@THAT
M=M-D
// add
@SP
A=M-1
D=M
A=A-1
M=M+D
D=A+1
@SP
M=D