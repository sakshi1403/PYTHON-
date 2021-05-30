'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''
Seconds = int(input("Enter number of second nedds to be converted(any integer value) =  "))
def conversion_to_hours():
    hours = int(Seconds/3600)
    
    return hours
H = conversion_to_hours()

def conversion_to_minutes():    
    minutes = int((Seconds%3600)/60)
    
    return minutes
M = conversion_to_minutes()

def conversion_to_seconds():    
    seconds = Seconds%60
    
    return seconds
S = conversion_to_seconds() 

print("There is/are",H, "hour(s).")
print("There is/are",M, "minute(s).")
print("There is/are",S, "second(s).")
 