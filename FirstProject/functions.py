# Function helps to stay dry: don't repast yourself
# --------------------------------------------- defining functions ---------------------------------------------------
def sing_happy_birthday():
    print("Happy birthday to you")
    print("Happy birthday to you")
    print("Happy birthday Dear you")
    print("Happy birthday to you")


sing_happy_birthday()


# ------------------------------------ return keyword in function ------------------------------------------------
# return exits the function
def square_of_7():
    return 7 * 7


print(square_of_7())

# ----------------------------- practice: coin flip --------------------------------------------------------------
from random import random


def flip_coin():
    if random() > 0.5:
        print("heads")
    else:
        print("tails")


flip_coin()
flip_coin()
flip_coin()


# ------------------------------------ function with parameters -----------------------------------------------------
def square(num):
    return num ** 2


print(square(2))
print(square(4))
print(square(8))


def happy_birthday(name):
    print("Happy birthday to you")
    print("Happy birthday to you")
    print(f"Happy birthday Dear {name}")
    print("Happy birthday to you")


happy_birthday("yash")
happy_birthday("falke")


# parameters vs arguments
# parameter is a variable in method definition
# When the method is called , arguments are the data that you pass into methods parameters


def divide(num1, num2):
    return num1 / num2


print(divide(2, 5))
print(divide(5, 2))


# ------------------------------------- Default parameters --------------------------------------------------------
# default parameters can be functions, lists, dictionary, strings or booleans, Anything!
def exponent(num, power=2):
    return num ** power


print(exponent(2, 3))
print(exponent(4, 8))
print(exponent(9))


def add(a, b):
    print(a + b)


def math(a, b, fn=add):
    return fn(a, b)


def subtract(a, b):
    return a - b


print(math(2, 2, add))
print(math(2, 2, subtract))


# -------------------------------------- keyword arguments ------------------------------------------------------
def full_name(first_name, last_name):
    print(f"Your full name is: {first_name} {last_name}")


full_name(first_name="yash", last_name="falke")
full_name(last_name="falke", first_name="yash")

# ---------------------------------------------- scope ---------------------------------------------------------------
# where our variables can be accessed
# variables created inside function are scoped in that function
# global scope: can be accessed anywhere in the function

total = 0


def counter():
    global total
    total += 1
    return total


# nonlocal: gives access to modify parents variable in child (aka nested) function
def outer():
    counter1 = 0

    def inner():
        nonlocal counter1
        counter1 += 1
        return counter1

    return inner()


# ------------------------------------------------ documenting functions --------------------------------------------
print(print.__doc__)


def exponent1(num, power=2):
    """exponent1(num, power) raises num to specified power . Power defaults to 2 """
    return num ** power


print(exponent1(2, 3))
print(exponent1.__doc__)
