numbers = input("Input Some Numbers(With space-betwen): ")
list = numbers.split(",")
tuple = tuple(list)
print('List: ' , list)
print("Tuple: ", tuple)

# Input: 1, 2, 3, 4, 5, 6, 7
# Output: List:  ['1', ' 2', ' 3', ' 4', ' 5', ' 6', ' 7']
#         Tuple:  ('1', ' 2', ' 3', ' 4', ' 5', ' 6', ' 7')