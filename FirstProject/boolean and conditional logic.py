# --------------------------------------- Conditional Statement ------------------------------------------------------
# If Elif else statement
name = input("Enter your name: ")
if name == "Arya Stark":
    print("Valar Morghulis")
elif name == "John Snow":
    print("You know nothing")
else:
    print("carry on")

# Multiple Elif
# casefold to convert into lowercase of its specific language
color = input("Enter your favourite color? ")
if color.casefold() == "purple":
    print("Excellent Choice")
elif color.casefold() == "teal":
    print("Not bad :)")
elif color.casefold() == "pure darkness":
    print("I like how you think")
elif color.casefold() == "seafoam":
    print("medicare")
else:
    print("You Monster!")

# ------------------------------------------ Truthiness and falseness ------------------------------------------------
# we can call values that will resolve to true as "Truthy" , or values resolve to false as "falsy"
# Things that are naturally falsy are: empty objects, empty strings, none and zero
# rest all itself are falsy
if 0:
    print('Yasyyy')

animal = input("Enter your favourite animal: ")
if animal:
    print(f"this {animal} is my favourite too")
else:
    print("You didn't say anything")

# ---------------------------------------- Comparison operators -------------------------------------------------------
print(1 == 1)
print('a' > 'A')
print(-100 > -200)
age = 18
if age >= 18:
    print("You are an ADULT")

# ------------------------------------------- Logical Operators ----------------------------------------------------
# LOGICAL AND - Both left and right operand should be true for TRUTHY
age = 6
#  age > 2 and age < 8
if 2 < age < 8:
    print("You Get child price")

# LOGICAL OR - Either one of the operand must be true for truthy
city = input("Where do you live? ")
if city.casefold() == "mumbai" or city.casefold() == "surat":
    print(f"Welcome to {city.casefold()} mere jan ke tote :) ")

# LOGICAL NOT - Truthy if opposite of operand is true
age = 10
# 2-8 2$ ticket
# >65 5$ ticket
# 10$ ticket for everyone else
if not (2 > age > 8 or age >= 65):
    print("You Pay 10 Dollars")
elif 2 > age > 8:
    print("You Pay 2 dollar ticket")
else:
    print("You pay 5 dollar ticket")

# ----------------------------------- is: used for Testing for equality -----------------------------------------------
a = 1
print(a == 1)  # checks values
print(a is 1)  # checks the exact same place of memory

# --------------------------------------- CODE-ALONG -----------------------------------------------------------------
# Bouncer
# ask for age
# 18 - 21 wristband , 21+ drink - normal entry , otherwise too young sorry
age = input("How old are you? ")
if age:
    age = int(age)
    if age >= 21:
        print("You are good to enter and you can drink")
    elif age >= 18:
        print("You can enter but need a wrist band!")
    else:
        print("You can't enter , little good one :(")
else:
    print("Please enter an age :(")
