# While is used when we have to run the loop until the condition is true and stop when condition is false
# While loop is used when you don't know in advance, how many times the loop will execute

i = 0   # i should always be initialised earlier before writing while loop
while i < 10:
    print(f"i is now in {i}")
    i += 1

exits = ["north", "south", "east", "west"]
chosenExit = ""
while chosenExit.casefold() not in exits:
    chosenExit = input("Enter the direction, to exit: ")
    if chosenExit.casefold() == "quit":
        print("Game over ...")
        break
print("Ohhh yeah ......., you have exited from the game mah boy .......")

# Guessing Game and Random Number Generator
import random
answer = random.randint(1, 10)
guess = int(input("Enter the number to guess (0 to exit the game): "))
while guess != answer:
    if guess == 0:
        print("Exited the Game")
        break
    else:
        if guess < answer:
            guess = int(input("Please guess higher: "))
        else:
            guess = int(input("Please guess lower: "))
if guess == answer:
    print("Voila, you had guessed the number correctly")

# for variable name separation we should use underscore no Capital letter
# This is done According to the PEP8 of python

# ------------------ else in the loop ----------------------------------
# Here the else loop will run only when the for loop ends normally without any break statement
numbers = [1, 45, 31, 15, 60]
for i in numbers:    # Reject the list
    if i % 8 == 0:
        print("The list is unacceptable ")
        break
else:
    print("The list is acceptable")

exits = ["north", "south", "east", "west"]
chosenExit = ""
while chosenExit.casefold() not in exits:                 # Application of else in while loop
    chosenExit = input("Enter the direction, to exit: ")
    if chosenExit.casefold() == "quit":
        print("Game over ...")
        break
else:
    print("Ohhh yeah ......., you have exited from the game mah boy .......")

# ------------------------- CHALLENGE ----------------------------------------
while True:
    print("Please choose your option from the list below: ")
    print("1.   Learn Python\n2.   Learn Java\n3.   Go Swimming\n4.   Have Dinner\n5.   Go to bed\n0.   Exit")
    option = input()
    if option in "12345":
        print("Thank you for choosing option no {}\n".format(option))
    elif option == 0:
        print("Exited Successfully")
        break
    else:
        print("You had chosen wrong option no i.e. {}\n".format(option))
