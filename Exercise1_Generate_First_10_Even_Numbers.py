# Excercise 1 - Generate the first 10 even numbers.
count = 0;
evenNum = 0; 
while ( count < 10) :
    evenNum = evenNum + 2 
    print ("The Even Numbers are :", evenNum)
    count = count + 1 

# Excercise 1 Variation - Generate the first 10 even numbers from input.
inputVal = int(input("Enter a value: "))
count = 0;
evenNum = inputVal;
listEvenNum = []
for i in range(1,10,1):
    if (evenNum % 2==1):
        evenNum = evenNum + 1
        listEvenNum.append(evenNum)
    evenNum = evenNum + 2
    listEvenNum.append(evenNum)    
            
print ("The Even Number Series is: ",listEvenNum);        
