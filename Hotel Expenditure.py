'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''
print("Welcome to SKYLINE RESORT AND HOTEL !")
print("Hope you enjoyed your vacay.")
print("Thankyou for letting us serve you. See you again.Hve a nice journey ahead !")
Type = input("Enter the type of room booked(Deluxe Room/Non AC Room) : ")
Days = int(input ("Enter the number of days spent :"))
Rooms = int(input ("Enter the number of rooms booked :"))
Food = float (input("Enter the total amount spent on food : Rs."))
def bill():
    if Type == "Deluxe Room":
        a = 7500*Rooms*Days
        b = float(0.09*Food)      # Half of the total tax i.e. 18 percent
        c = float(0.1*Food)       #Tip
        d = float(Food+(2*(b))+c) # Meal Payment
        x = float(a+d)            # Total Payment
        print("Total room tariff payable for %d days : Rs. %d " %(Days,a))
        print("Amount spent on meals : Rs. %f" %(Food))
        print("SGST on meal is 9 percent : Rs. %f" %(b))
        print("CGST on meal is 9 percent : Rs. %f" %(b))
        print("Tip given on meal is 10 percent : Rs. %f" %(c))
        print("Total tariff payable on meal : Rs. %f" %(d))
        print("Total payable bill : Rs. %f" %(x))
    elif Type == "Non AC Room":
         e = 4500*Rooms*Days
         f = float(0.025*Food)     # Half of the total tax i.e. 5 percent
         g = float(0.1*Food)       # Tip
         h = float(Food+(2*(f))+g) # Meal Payment
         y = float(e+d)            # Total Payment
         print("Total room tariff payable for %d days : Rs. %d " %(Rooms,e))
         print("Amount spent on meals : Rs. %f" %(Food))
         print("SGST on meal is 2.5 percent : Rs. %f" %(f))
         print("CGST on meal is 2.5 percent : Rs. %f" %(f))
         print("Tip given on meal is 10 percent : Rs. %f" %(g))
         print("Total tariff payable on meal : Rs. %f" %(h))
         print("Total payable bill : Rs. %f" %(y))

    else:
        print("Enter a valid choice !")
bill()   