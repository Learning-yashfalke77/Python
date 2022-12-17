# Variables are like containers , store some data and pull it out later, They can hold all sorts of things ,
# like boolean numbers and strings
num_of_cats = 22  # creation of variable with assignment
print(num_of_cats)
num_of_cats = num_of_cats * 2  # reassignment of variable
print(num_of_cats)

al, at, once = 33, 100, 5  # assignment and creation of variables at same time
print(al, at, once)

# -------------------------------- variables naming conventions -------------------------------------------------------
# 1) Variables must start with letters or underscore
# 2) rest of the name must consist letters, numbers and underscores
# 3) Names are case-sensitive
# 4) underscores should be there between words
# 5) Most variables must be lower-case only, 'Constant' must be upper case, 'class' must be UpperCamelCase
# 6) Variables with two underscores(Dunder) must be left alone , should not be changed
# 7) In reassigning we can change variable data type from string to int etc....

# -------------------------------------- Python is dynamically Typed -------------------------------------------------
# We can reassign variables to different types
awesomeness = True
print(awesomeness)
awesomeness = "YOLO"
print(awesomeness)
awesomeness = None
print(awesomeness)

# ----------------------------------------- None dataType in Python --------------------------------------------------
name = None
print(type(name))

# ----------------------------------------- String datatype in Python -------------------------------------------------
# String literals in python can be defined with single or double quote
my_other_str = 'a hat'
my_str = "a cat"
print(my_other_str, my_str)
msg = "He said 'Hello There!' "  # A double quote with single quote
print(msg)

# String escape Character / sequences
msg = "hello\nworld"  # creates a new line inside string
print(msg)
msg = "this is a backSlash : \\"  # To show backslash, otherwise it will consider start of escape sequence
print(msg)

# String Concatenation
username = "yashmak77"
print("Hello There!, Welcome to game :) " + username)
# print(8 + "hello")  # error for concatenation dataType should be same
name = "yash"
name += "falke"  # similar for multiplication and division for numbers also
print(name)

# Formatting Strings i.e. string interpolation
# 1) Method 1 using "F String" only above 3.6 python
x = 10
msg = f"I Told you {x} times that you are incorrect"
print(msg)
msg = f"I Told you {x + 1} times that you are incorrect"
print(msg)
pi = 22 / 7
print(f"The Value of pi is {pi:12.02f}")  # formatting number with 12 digit space and 50 decimal precision

# 2) Method 2 using .format method or replacement field
print("""January {0}
February {1}
March {0}
April {2}
May {0}
June {2}                             
July {0}
August {0}
September {2}
October {0}
November {2}
December {0}""".format(31, 28, 30))
print('The value of pi is {:2.20}'.format(pi))  # in replacement field {position:width.decimalPointPrecision}
for i in range(1, 12):
    print("No. {} squared is {:2} and cubed is {:4}".format(i, i ** 2, i ** 3))
    print("No. {} squared is {:<2} and cubed is {:<4}".format(i, i ** 2, i ** 3))  # for formatting on right-hand side

# 3) older way in python 2 deprecated in python 3 Using %
age = 18
print("My age is %d, %s and %d, %s" % (age, "years", 6, "months"))
print("PI is approximately %12.50f " % (22 / 7))

# Indexing in strings
name = "chuck"
print(name[0])  # starts from left
print(name[-1])  # starts from right

# ---------------------------------------- Converting Data Type -----------------------------------------------------
# you can explicitly convert variables into by using the name of built-in type as a function
decimal = 12.564634
integer = int(decimal)  # converting float into integer
print(integer)
print(float(integer))  # converting integer into float
print(str(integer))  # converting integer into string

# ------------------------------------------ input in python -------------------------------------------------------
# there is a built-in function in python called 'input' that will prompt the user and store the result to variable
# Input always store data in the form of string
data = input("Enter your favourite color? ")
print(data)

# ---------------------------------------- Practice of all above concept --------------------------------------------
# kilometers to mileage converter
print("How many kilometers did you cycled today?")
kms = float(input())
miles = round(kms / 1.60934, 2)  # rounding the no up-to 2 digit places
print(f"That is equal to {miles} miles")
