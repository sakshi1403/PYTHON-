listA = []
listB = []
x = int(input(" Enter the range to form a larger list: "))  # range
print("Please insert Elements for forming larger list ony by one : ")

for i in range(x):  # loop for list formation
    y = int(input("Enter number : "))
    listA.append(y)

print(" LIST: ", listA)

x = int(input(" Enter the range for forming a smaller list :"))
print("Please enter Elements for generating larger list ony by one : ")

for i in range(x):
    y = int(input("Enter number : "))
    listB.append(y)


def checksublist():
    a = 0
    # check element of second list into first list
    for elem in listB:
        if elem in listA:
            a = 1

    # checking condition
    if a == 1:
        print("True")
    elif (len(listB)) == 0:
        print("True")

    else:
        print("False")


checksublist()