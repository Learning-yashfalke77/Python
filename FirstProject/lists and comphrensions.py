# if we want to convert a data type items in list use list comprehensions
nums = [1, 2, 3]
print([x * 10 for x in nums])
print([x / 2 for x in nums])

# using string
name = "yash"
print([char.upper() for char in name])

# using range
print([num * 10 for num in range(1, 10)])

# using bool
print([bool(value) for value in [0, [], '']])

# ------------------------------- Conditional with list comprehension  --------------------------------------------
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print([num for num in numbers if num % 2 == 0])
print([num for num in numbers if num % 2 != 0])

# using if else
print([num * 2 if num % 2 == 0 else num / 2 for num in numbers])
# print list of num*2 if num is even , else print list of num/2

with_vowels = "this is so much fun"
print(''.join([char for char in with_vowels if char not in "aeiou"]))

# -------------------------------------- nested list comprehension ----------------------------------------------------
nested_lists = [[1, 2, 3], [4, 5, 6, ], [7, 8, 9]]
# to print value of each lists
[[print(value) for value in liste] for liste in nested_lists]
