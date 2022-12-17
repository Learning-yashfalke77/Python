# ---------------------------------------------- Error types --------------------------------------------------------
# 1) Syntax Error
# occurs when python encounters incorrect syntax

# 2) Name Error
# this occurs when variable is not defined i.e. it hasn't been assigned

# 3) Type error
# when there is mismatch of data types

# 4) Index Error
# Occurs when you try to access the element in a list using invalid index

# 5) Value Error
# This occurs when a built-in operation or function receives an argument that has a right type but in appropriate value
# int("foo")  # gives value error

# 6) keyError
# this occurs when a dictionary does not have specific key

# 7) Attribute Error
# This occurs when a variable does not have attribute
# [1, 2, 3].hello()    #attribute error

# ------------------------------------- Raising our own error --------------------------------------------------------
# raise ValueError("invalid value :(")
def colorize(text, color):
    colors = ("cyan", "yellow", "blue", "green", "magenta")
    if type(text) is not str:
        raise TypeError("Text must be String")
    if type(color) is not str:
        raise TypeError("color must be String")
    if color not in colors:
        raise ValueError("color should be of any one color of rainbow")
    print(f"Printed {text} in {color} color")


colorize("yash", "blue")
# colorize("falke", "brown")

# ------------------------------------- handling errors ----------------------------------------------------------
# try:
#     foobar
# except:
#     print("problem")

d = {"name": "ricky"}


def get(dicto, key):
    try:
        return d[key]
    except KeyError:
        return None


print(get(d, "city"))
print("after the try")

# ------------------------------- try except else finally ------------------------------------------------------------
try:
    name = int(input("Enter the number"))
except ValueError:
    print("That is not a number")
else:
    print("I am in the else")
    print("I will run if except does not run")
finally:
    print("runs no matter what")
