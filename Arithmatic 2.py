'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''
Chocolates = int(input("Enter number of chocolates available =   "))
Candies = int(input("Enter number of candies available =  "))
Soft_Drinks = int(input("Enter number of soft drinks available =  "))
People = int(input("Enter  total number of people in a party =  "))
Adults = int(input("Enter number of adults in a party "))
Parties = int(input("Enter  total number of parties in a city  "))
def Sum():
    rewards = Chocolates + Candies + Soft_Drinks 
    
    return rewards
    

s=Sum()

def Difference():
    kids=People-Adults

    return kids

dif=Difference()


def division():
    packets=s//dif

    return packets

div=division()


def product():
    return div*Parties


p=product()



print("Total number of rewards=",s)
print("Total number of kids in party=",dif)
print("Total number of packets each kid own=",div)
print("Total number of packets needed for party in city=",p)
