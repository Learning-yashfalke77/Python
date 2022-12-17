# SEQUENCES IS THE ORDERED COLLECTION OF ITEMS
# TODO: Source for sequences https://docs.python.org/3/library/stdtypes.html#sequence-types-list-tuple-range
# Lists are mutable sequences, typically used to store collections of homogeneous items
# lists are intended to be homogeneous, but we can store different type but difficulty comes in processing the list
# for eg join method

# ---------------------------------------LISTS--------------------------------------------------------
computer_parts = ["Computer",
                  "Monitor",
                  "Keyboard",
                  "Mouse",
                  "Mouse Mat"
                  ]
for part in computer_parts:
    print(part)
print()
print(computer_parts[2])
print(computer_parts[0:3])
print(computer_parts[-1])
print()
#
computer_parts += ["printer"]  # concatenating a new value to the list at last position
print(computer_parts)

a = b = c = d = e = computer_parts  # Chain Assignment
# Only 1 list is present and all these names are bound to that same object
print("Adding scanner to the list ")
a.append("scanner")  # concatenating a new value to the list at last position
print(a)
print(b)
print(c)

# Built in functions for all common sequences
# TODO: References https://docs.python.org/3/library/stdtypes.html#mutable-sequence-types
even = [2, 4, 6, 8]
odd = [1, 3, 5, 7, 9]
print("The Minimum and Maximum of even numbers in 1 to 10 is {} and {} ".format(min(even), max(even)))
print("The Minimum and Maximum of odd numbers in 1 to 10 is {} and {}".format(min(odd), max(odd)))

print()
print(len(even))  # Gives the length
print(len(odd))

print()
print("Mississippi".count("iss"))  # counts how many times does the word mississippi comes

# Built in functions for Mutable sequences

# Application of append method in list
available_parts = ["computer",
                   "monitor",
                   "keyboard",
                   "mouse",
                   "mouse mat",
                   "hdmi"
                   ]
current_choice = "-"
computer_parts = []

while current_choice != "0":
    if current_choice in "123456":
        print("Adding {}".format(current_choice))
        if current_choice == "1":
            computer_parts.append("computer")
        elif current_choice == "2":
            computer_parts.append("monitor")
        elif current_choice == "3":
            computer_parts.append("keyboard")
        elif current_choice == "4":
            computer_parts.append("mouse")
        elif current_choice == "5":
            computer_parts.append("mouse mat")
        else:
            computer_parts.append("hdmi")
    else:
        print("Please choose your option from the list below: ")

        for parts in available_parts:  #
            # This is not efficient because here we have to 1st find that part then its index number which is not good
            # for big lists
            print("{}:  {}".format(available_parts.index(parts) + 1, parts))

#         # another way using enumerate function which gives directly that particular part with its index number
        for number, parts in enumerate(available_parts):
            print("{}:  {}".format(number + 1, parts))
    current_choice = input()
print(computer_parts)
print()

# Another example of enumerate (It can be used with any sequence)
for number, character in enumerate("abcdefgh"):
    print(number, character)

# improving the computer parts program
available_parts = ["computer",
                   "monitor",
                   "keyboard",
                   "mouse",
                   "mouse mat",
                   "hdmi"
                   ]

valid_choices = []
for i in range(1, len(available_parts) + 1):
    valid_choices.append(str(i))

current_choice = "-"
computer_parts = []

while current_choice != "0":
    if current_choice in valid_choices:
        index = int(current_choice) - 1
        chosen_part = available_parts[index]
        if chosen_part in computer_parts:        # if the choice value is already present then remove it
            print("Removing {}".format(current_choice))
            computer_parts.remove(chosen_part)          # remove items from list
        else:
            print("Adding {}".format(current_choice))
            computer_parts.append(chosen_part)
        print("Your list now contains {}".format(computer_parts))
    else:
        print("Please choose your option from the list below: ")
        for numbers, parts in enumerate(available_parts):
            print("{}:  {}".format(numbers + 1, parts))
        print("0:  Exit")
    current_choice = input()
print(computer_parts)

# TODO: ALL BUILT - IN FUNCTIONS IN PYTHON: https://docs.python.org/3/library/functions.html

# Creating Lists
even = [2, 4, 6, 8]
odd = [1, 3, 5, 7, 9]
numbers = even + odd

lists1 = list("122344566654")
print(lists1)

# There 12 methods to copy a lists but all are not that much efficient
# TODO: the 12 ways with efficiency is :
# TODO https://stackoverflow.com/questions/2612802/list-changes-unexpectedly-after-assignment-how-do-i-clone-or-copy
# TODO -it-to-prevent/43220129#43220129
# but copy inbuilt method is the most efficient way to do so
more_numbers = numbers[:]
print(more_numbers)
more_numbers = numbers.copy()
print(more_numbers)

# --------------------------------------------------------------------------------------------------------------------

# Application of slicing in Mutable Sequences
computer_parts = ["Computer",
                  "Monitor",
                  "Keyboard",
                  "Mouse",
                  "Mouse Mat"
                  ]

computer_parts[3] = "Trackball"  # replacing mouse with track ball
computer_parts[3:] = ["Trackball"]  # replacing two values in list with one values

# --------------------------------------------------------------------------------------------------------------------

# Deleting items in a list (For Ordered)
data = [4, 5, 104, 105, 110, 120, 130, 130, 150, 160, 170, 183,
        185, 187, 188, 191, 350, 360]
del data[0:2]  # excluding 2nd position, removing starting 2 items from lists
print(data)

del data[14:]  # removing last 2 items from lists
print(data)

# remove numbers in a list in a given sequence
min_value = 100
max_value = 300
stop = stop1 = 0
for index, values in enumerate(data):    # remove/process low values in the list
    if values > min_value:
        stop = index
        break

del data[:stop]
print(data)

# To remove/process high values in the list in sorted order
for index in range(len(data) - 1, -1, -1):
    if data[index] <= max_value:
        stop1 = index + 1            # line to delete is one after index
        break

del data[stop:]
print(data)

# -------------------------------------------------------------------------------
# edge case: testing your code with different possibilities to break it
# corner case: testing your code with special case eg: dividing number by 0
# -------------------------------------------------------------------------------
# Deleting items in a list (For UnOrdered)
data = [104, 101, 4, 105, 308, 103, 5, 107, 100, 306, 106, 102, 108]
min_value = 100
max_value = 200

# removing all outlying values highest as well as lowest
for index in range(len(data) - 1, -1, -1):
    if (data[index] < min_value) or (data[index] > max_value):
        del data[index]
print(data)

# by using reverse iterator  function
top_index = len(data) - 1
for index, values in enumerate(reversed(data)):   # here index will remain same only the values gets reversed
    # so last number will have 0 index position by using reversed function
    print((top_index - index), values)

