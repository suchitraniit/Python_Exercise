# Excercise 2 - Input a number and check if it is prime or not
                # Defenition of prime number, any number that is divisible by its
                # 1 and its own number i.e its divided by any other number, the reminder should be 0
                
inputVal = int(input("Enter a number for prime check: "));
isPrime = 1
if inputVal > 1 :
    i = 2; 
    while(i< inputVal):
        if (inputVal % i == 0):
            print ("number ", inputVal, " is not a prime number")
            i = i + 1
            isPrime = 0;
            break;
        i = i+1
if (isPrime ==1):
    print ("number ", inputVal, " is a prime number")
