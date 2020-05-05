# CHALLENGE:
 + The assembly dump of of 2 functions f1 and f2 stored in a files "f1.out" and "f2.out" respectively
 + There is an instruction which is roughly equivalent to 
 + X = address(Y*4 + Z)
 + where X,Y,Z are all 64 bit general purpose registers.
 + Find the address of this instruction and place it within the brackets of 'ctf{}'

# Register nomenclature
 + in x86 architecture, registers are used with the following nomenclature
 + ![](GPRs.png)
 + credits: Lecture slides for Problem Solving Skills for Engineers - I by Narasimha Datta and Channa Bankapur 

# lea (load effective address) instruction:
 + the lea instruction works as follows:
 	+ lea -3(%rbx,%rbx,8),%rax translates to 
 		+ %rax = address (%rbx * 8 + %rbx) - 3
 		+ viz =>  %rax = address (%rbx * 9) - 3
 	+ the instruction corresponding to this in f1.out is lea 0x0(%rbp,%rax,4),%rdi
 	+ this translates to %rdi = (%rbp * 4 + %rax) + 0
 	+ here %rdi, %rbp, %rax are X, Y, Z respectively

# Reference notes
 + https://cs.lmu.edu/~ray/notes/x86overview/

