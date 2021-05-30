'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''
M = float(input("Enter the value of Richter Scale  "))

#comparing the intensities of Earthquake with base Earthquake
#R = i:i(knot),i is intensity of occurred Earthquake while i(knot) is intensity of base Earthquake

def intensity():
    i = 10**M
    
    return i
I = intensity()    

print("Thus intensity of Earthquake occurred is" ,I, "times intenser than the intensity of base Earthquake")
    
    
    