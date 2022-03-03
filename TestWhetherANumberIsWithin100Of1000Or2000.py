def checkMe(n):
    return (abs(1000 - n) <= 100  or abs(2000 - n) <= 100)
    
num = int(input("Enter the number: "))
print(checkMe(num))
