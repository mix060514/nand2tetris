// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Fill.asm

// Runs an infinite loop that listens to the keyboard input.
// When a key is pressed (any key), the program blackens the screen,
// i.e. writes "black" in every pixel;
// the screen should remain fully black as long as the key is pressed. 
// When no key is pressed, the program clears the screen, i.e. writes
// "white" in every pixel;
// the screen should remain fully clear as long as no key is pressed.

// Put your code here.
// 1 row have 32 col

// rows = 256 / 16 = 16
// cols = 512 / 16 = 32
// screen_value = 0
// while True:
//     if kbd != 0:
//         screen_value = -1
//     else:
//         screen_value = 0
//     for r in range(rows):
//         for c in range(cols):
//             SCREEN + r * 32 + c = screen_value
    // initial
    @screen_value 
    M=0
    @r 
    M=0
    @c 
    M=0
    @pos 
    M=0

(Loop)
    @kbd 
    D=M
    @Keyboard_True
    D;JNE

    @screen_value
    M=0

    @Draw 
    0;JEQ

(Keyboard_True)
    @screen_value
    M=-1

    @Draw 
    0;JEQ

(Draw)


(For_r)






(For_c)
    @32
    D=A
    @r 
    D=D*M
    @pos 
    M=D

    @c
    D=M
    @pos 
    M=D+M

    @SCREEN 
    D=M
    @pos 
    M=D+M








(For_c_end)




    @For_c
    ;J


    @c 
    M=M+1
(For_r_end)
    @r 
    M=M+1


    @Loop
    0;JEQ

