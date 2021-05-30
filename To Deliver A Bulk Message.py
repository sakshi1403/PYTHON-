'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''
n = int(input("Enter the number of students = "))
names=[]
Admission_ID=[]
CAP_Rank=[]
for i in range(n):
    a = input("Enter the name of student ")
    names.append(a)
    
    b = input("Enter the Admission_ID ")
    Admission_ID.append(b)
    
    c = int(input("Enter the CAP_Rank "))
    CAP_Rank.append(c)
for i in range(len(names)):   
    print("Hi %s" %(names[i]))
    print("Congratulations...! %s, you got selecteD for next round of recruitment process." %(names[i]))
    print("Submit your academic credential including primary and secondary certificates.")
    print("Your admission ID is %s and will be eligible for the next round of interview with a CAP rank. of %d " %(Admission_ID[i],CAP_Rank[i]))
    print("If you submit all the documents on time and process university might offer you a scholarship.")
