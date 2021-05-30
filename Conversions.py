'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''
seconds = int(input("Input seconds  "))
Hours = int(seconds/60/60) 
Minutes = int((seconds%3600)/60 )hmetic.p
Seconds = seconds%60 
print("Hours spent = ",Hours)
print("Minutes spent = ",Minutes)
print("Seconds spent = ",Seconds)
