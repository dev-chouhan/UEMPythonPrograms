value = int(input("Enter the value: "))
n1 = int("%s" % value)
n2 = int("%s%s" % (value, value))
n3 = int("%s%s%s" % (value, value, value))
print(n1 + n2 + n3)