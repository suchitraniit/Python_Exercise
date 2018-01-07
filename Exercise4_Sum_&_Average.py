# Exercise 4 - Input 10 numbers and display the sum and average 
lstVal = []
sumVal = 0
avgVal = 0
for i in range(0,10,1):
    inputNum = int(input("Enter value #: "))
    lstVal.append(inputNum)
    sumVal = inputNum + sumVal
avgVal = (sumVal/10) 
print("The sum is ", sumVal)
print("The average value is ", avgVal)
