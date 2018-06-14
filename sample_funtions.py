uservalue = input("Enter a value to get factorial:")

def fact(number):
    factorial = 1
    if number < 0:
        print ("factorial doesnot exist for negative numbers")
        exit()
    elif number == 0:
        print ("Factorial of 0 is 1")
        exit()
    else:
        for i in range(1, number + 1):
            factorial = (factorial*i)
        print factorial
    return ;


fact(uservalue)
