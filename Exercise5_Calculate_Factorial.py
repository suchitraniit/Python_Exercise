#Excercise5: Input a number and calculate its factorial 
inputVal = int(input("Enter a number to calculate its factorial: "))
factRes = 1
if (inputVal == 0):
    print ("The factorial for this number is 0")
else:
    i = 0 
    for i in range(inputVal,0,-1):
        factRes = factRes * i
    print ("The factorial for the number ",inputVal, " is ", factRes)
