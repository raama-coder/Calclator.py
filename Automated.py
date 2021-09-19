print("Welcome to this Calculator app.")
print("Press '1' to do Addition. Press '2' to do Subtraction. Press '3' to Multiply. Press '4' to Divide.")

Choice=int(input("Choose what Operation you want: "))
x=int(input("Enter The First Number: "))
y=int(input("Enter The Second Number: "))

Add=x+y
Subtract=x-y
Multiply=x*y
Divide=x/y

if Choice == 1:
    print("The Added Number is:",Add)
elif Choice == 2:
    print("The Subtracted Number is:",Subtract)
elif Choice == 3:
    print("Your Multiplied Number is:",Multiply)
elif Choice == 4:
    print("Your Divided Number is:",Divide)
else:
    print("The Operation is invalid") 