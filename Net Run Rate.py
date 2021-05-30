'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''
print("To calculate Net Run Rate of team score(runs) and overs are needed. Overs are required in whole numbers but number of balls needs the input as below")
print("There are 6 baals in an over ")
print("1/6 balls = 0.167 balls, 2/6 balls = 0.034 balls, 3/6 balls = 0.5 balls, 4/6 balls = 0.67 balls, 5/6 balls = 0.834 balls and 6/6 balls = 1 over   ")

score_A = int(input("Enter runs scored by Team BRAIN "))
overs_A = float(input("Enter overs needed to score a target by Team BRAIN "))

score_B = int(input("Enter runs scored by Team HEART "))
overs_B = float(input("Enter overs needed to score a target by Team HEART "))

NRR_A = float(score_A/overs_A - score_B/overs_B)
NRR_B = float(score_B/overs_B - score_A/overs_A)

if NRR_A>NRR_B:
    print("BRAIN wins over HEART")
    print("POSITION TEAM   NET RUN RATE")
    print("1.       BRAIN",NRR_A)
    print("2.       HEART",NRR_B)
elif NRR_B>NRR_A:
    print("HEART wins over BRAIN")
    print("POSITION TEAM   NET RUN RATE")
    print("1.       HEART",NRR_B)
    print("2.       BRAIN",NRR_A) 
else:
    print("Well tried!")
    print("But HEART and BRAIN have to play more to decide the winner ")



