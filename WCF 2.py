'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''
T  = float(input("Enter Air Temperature in Celcius(between -45°C to 10°C only.) "))
v = float(input("Enter wind velocity in km/hr "))

def Twc():
    wcf = 13.12 + (0.6215)*T - (11.37)*(v)**0.16 + (0.3965)*(T)*(v)**0.16
    
    return wcf

w = Twc()    
print("The Wind Chill Factor(Fahrenheit) for a Air Temperature in celcius and Wind Velocity in km/hr is ",w)
 