##This is a sample program to check the number is prime number or odd number
uservalue = input("Enter a value to check whether it is even or odd:")
value = uservalue%2
#print value
if uservalue == 0:
    print("Number entered is ZERO and it is even number")
elif value == 0:
    print ("Number entered in EVEN number")
else:
    print ("Number entered is ODD number")
