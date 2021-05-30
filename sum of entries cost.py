'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''
print( "We Welcome all the people as well as guests in this SCIENCE EXHIBITION")
a = 0
def AgeDistribution():
    global a
    age_entry = int(input("Please enter the age of the guest: "))
    if 0< age_entry <5:
        a = a + 0 
    elif 5<= age_entry <=15:
        a = a + 20
    elif 15< age_entry <60: 
        a = a + 60
    elif 60<= age_entry: 
        a = a + 40
    print("Total cost value of people enterd in up til now   = Rs. %.2f" % (a))
    AgeDistribution()

AgeDistribution()
