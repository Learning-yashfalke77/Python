# SORTING IN LISTS  (For mutable sequences)
even = [2, 4, 6, 8]
odd = [1, 3, 5, 7, 9]

even.extend(odd)   # appends all the values of odd to the even
print(even)

even.sort()    # sorts the elements of list in ascending order
print(even)

even.sort(reverse=True)  # sorts the element in reverse order
print(even)

# here the sorting is done and changes is done to that lists only no new copy of list is created

# -------------------------------------------------------------------------------------------------------------------

# It always gives list in a sorted order
# Here another list is created
pangram = "The quick brown fox jumps over the lazy dog"
letters = sorted(pangram)
print(letters)

numbers = [2.3, 4.5, 8.7, 3.1, 9.2, 1.6]
print(sorted(numbers))

# case insensitive sort
pangram = "The quick brown fox jumps over the lazy dog"
letters = sorted(pangram, key=str.casefold)
print(letters)

# here do not type parenthesis in the key

names = ["Yash",
         "Medha",
         "jalander",
         "manisha"
         ]
names.sort(key=str.casefold)
print(names)

