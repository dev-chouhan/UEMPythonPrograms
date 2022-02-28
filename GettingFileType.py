fileName = str(input("Enter file name with it's extension: "))
fileType00 = fileName.split(".")
print("The Extention of "+fileName+" is: " + repr(fileType00[-1]))
# here “repr” stands for representation, it will bring required text under single-quotes
# here we use [-1] bcoz, it will always give you the last value after last dot
# Input:  myFile.java.txt
# Output: txt