num1 = 17
num2 = int(input("Enter second number: "))
difference = num2 - num1

if difference>0:
    print(difference * 2)
elif difference<0:
    print(abs(difference))
else:
    print("Please enter another number")
