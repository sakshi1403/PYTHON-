'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''

Integer=int(input("Enter an integer ")) 
Number=2  
while Number<Integer:
    Z = 0
    while Z<Number:
        Z = 0
        x = 1
        while x<Number:
                    
            if Number % x==0:
                Z = Z+x
            x = x + 1 
        if Z < Number:
            print(Number,"is Deficient")
        elif Z > Number:
            print(Number,"is Abundant")
        else:
            print(Number,"Number is Perfect!")
                        
        Number = Number + 1 