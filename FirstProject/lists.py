# It's just a collection or grouping of items
# --------------------------------------- Create List ---------------------------------------------------------------
demo_list = ["a", 1.45, True, 6.777]
print(demo_list)
print(len(demo_list))  # len gives the length of string
r = list(range(1, 10))
print(r)

# ------------------------------------- Accessing the data in List ----------------------------------------------------
friends = ["yash", "Yash", "YaSh"]
print(friends[0])
print(friends[1])
print(friends[2])
# print(friends[3])  # Gives Index Error

# Negative number index backwards
print(friends[-1])

# Check value in list
print("yash" in friends)
print("YASH" in friends)

# ------------------------------------- Iterating Over Lists -----------------------------------------------------
numbers = [1, 2, 3, 4]
# using for loop
for num in numbers:
    print(num)

# using while loop
i = 0
while i < len(numbers):
    print(numbers[i])
    i += 1

# ------------------------------------ Built In Methods in list --------------------------------------------------
# 1) append: add item to end of list
# append only one item to list
data = [1, 2, 3]
data.append(4)
print(data)

# 2) extend: add item to end of list all values passed to extend
data.extend([5, 6, 7, 8])
print(data)

# 3) insert: insert an item at given position
data.insert(2, "Hi")  # insert at 2nd index position starting from 0
print(data)

# 4) clear: remove all the items at once (The Least method used)
data.clear()
print(data)

# 5) pop: remove item at given position in list and return it
# If no index specified , removes and returns last items in the list
data = [1, 2, 3, 4]

last_item = data.pop()  # removed last item in list
print(data, last_item)

second_item = data.pop(1)
print(data, second_item)

# 6) remove: removes the first item from the list whose value is x
# Throws a value error if item is not found
data.remove(3)
print(data)

# 7) index: returns the index of specified item in list
print(data.index(1))

numbers = [5, 5, 6, 7, 5, 8, 8, 9, 10]
print(numbers.index(5))  # gives first occurrence of 5
print(numbers.index(5, 1))  # find 5 after index 1
print(numbers.index(5, 2))  # find 5 after index 2
print(numbers.index(8, 6, 8))  # find the no 8 between index 6 and 8

# 6) count: returns the number of times x appeared in the list
print(numbers.count(5))

# 7) reverse the elements of list in place
numbers.reverse()
print(numbers)

# 8) sort: sort items in ascending order
numbers.sort()
print(numbers)

# 9) join: It's a string video
# join converts from list to string
words = ["coding", "is", "simple"]
print(' '.join(words))

# -------------------------------------------- Slicing in Lists -------------------------------------------------------
# make new list from the slices of the old list
# syntax:  some_list[start:end:step]
# and end is exclusive
first_list = [1, 2, 3, 4, 5, 6]
# start
print(first_list[1:])
print(first_list[3:])
print(first_list[-1:])
print(first_list[-3:])
# end
print(first_list[:2])
print(first_list[:4])
# using both start and end
print(first_list[1:4])
print(first_list[1: -1])
# using step
print(first_list[1::2])

# reverse a string
print("this is fun"[::-1])

# -------------------------------------------------- Swapping values i lists--------------------------------------------
names = ["james", "Michelle"]
names[0], names[1] = names[1], names[0]
print(names)
