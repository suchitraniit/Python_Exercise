# Exercise 3 - Input 10 numbers and display the smalest and largest of them
lstVal = []
for i in range(0,10,1):
    inputNum = int(input("Enter value #: "))
    lstVal.append(inputNum)
print("The Maximum value is ", max(lstVal))
print("The Minimum value is ", min(lstVal))
