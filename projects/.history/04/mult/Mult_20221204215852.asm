// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Mult.asm

// Multiplies R0 and R1 and stores the result in R2.
// (R0, R1, R2 refer to RAM[0], RAM[1], and RAM[2], respectively.)
//
// This program only needs to handle arguments that satisfy
// R0 >= 0, R1 >= 0, and R0*R1 < 32768.

// Put your code here.
// int R0
// int R1
// int ans(R2) = 0
// int i = 0
// for (int i = 0; i<R1; i++){
//     ans += R0;
// }
// return ans 

    @R2
    M=0

    @i
    M=0 // i = 0
(Loop)
    // i < R1
    @R1
    D=M
    @i
    D=D-M
    @End
    D;JGE

    // R2 += R0
    @R0
    D=M
    @R2 
    M=D+M

    // i++
    @i 
    M=M+1

(End)
    @End 
    0; JEQ

