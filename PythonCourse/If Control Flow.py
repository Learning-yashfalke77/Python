name = input("Hello there, Enter your name: ")
age = int(input("How old are you, {0}? ".format(name)))

# IF ELSE
if age >= 18:  # Here : is used for indentation FROM NEXT LINE
    print("You are Old enough to vote")
else:
    print("You can't vote, Please come back in {} years".format(18 - age))

# ELIF
if 18 <= age <= 100:
    print("You are old enough to vote ")
    print("Put an X in the box")
elif age > 100:
    print("Sorry {0}, You have died ".format(name))
else:
    print("You can't vote, Please come back in {} years".format(18 - age))

# Guessing Game
number = 5
guess = int(input("Enter the number between 1 to 10: "))

if guess < number:
    print("Please guess higher")
    guess = int(input())
    if guess == number:
        print("Well done , You have guessed ")
    else:
        print("Sorry you have not guessed correctly, pls play again")
elif guess > number:
    print("Please guess lower")
    guess = int(input())
    if guess == number:
        print("Well done , You have guessed ")
    else:
        print("Sorry you have not guessed correctly, pls play again")
else:
    print("You have guessed the right number at first glance  ")

# avoiding duplication
if guess != number:
    if guess < number:
        print("Please guess higher")
    else:  # Guess must be greater than answer
        print("Please guess Lower")
    guess = int(input())
    if guess == number:
        print("Well done , You have guessed ")
    else:
        print("Sorry you have not guessed correctly, pls play again")
else:
    print("You have guessed the right number at first glance ")

# -----------------------------------------------------------------------------------------------------

# AND OR
age = int(input("How Old are you?????? "))
# if age >= 16 and age <= 60:                     using and
if 16 <= age <= 60:                          # using simplified chained comparison
    print("Have a good day at Work")   # Python will stop checking as soon as it finds a condition false
else:
    print("Enjoy your free time")
print("-" * 80)
if age < 16 or age > 65:                    # using or
    print("Enjoy your free time ")    # Python would stop checking as soon as it finds one that is true
else:
    print("Have a good day at Work")

day = "Saturday"
temperature = 30
raining = True
if (day == "Saturday" and temperature > 27) or not raining:
    print("You can go to swimming ")
else:
    print("Learn python ")

# Operator precedence
# and then or then not

# Truthy and falsy values
# 0, False and empty sequences including string always contains false values
if 0:                     # only 0 means checking if 0==true
    print("True")
else:
    print("False")

name = input("Enter your name ")
if name:                  # checking if name == true means if name is empty then false else true
    print(f"Hello {name}, How are you?")
else:
    print("You are man with no name ")

# ---------------------------------- IN --------------------------------------------
parrot = "Norwegian Blue"
letter = input("Enter the letter: ")
if letter in parrot:
    print("{} is in {} ".format(letter, parrot))
else:
    print("I don't need that letter ")

# --------------------------- NOT IN ---------------------------
activity = input("What would you like to do today ")
if "cinema" not in activity.casefold():  # here casefold convert all letters into lowercase
    print("But i want to go to the cinema ")

# TODO: all other inbuilt methods of string --> https://docs.python.org/3/library/stdtypes.html#string-methods

# --------------------------- Challenge --------------------
name = input("Please enter your name: ")
age = int(input(f"Hello {name}, Enter your age: "))
if 18 <= age <= 30:
    print("Welcome to the holidays ")
else:
    print(f"You are underage pls try again")
