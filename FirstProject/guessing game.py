import random

random_number = random.randint(1, 10)  # Here end is inclusive
while True:
    guess = int(input("Pick a number from 1 to 10: "))
    if guess > random_number:
        print("Too High :(")
    elif guess < random_number:
        print("Too Low :( ")
    else:
        print("You won :) ")
        play_again = input("Do you want to play again? ")
        if play_again == "y":
            random_number = random.randint(1, 10)  # Here end is inclusive
            guess = None
        else:
            print("Thank you for playing")
            break

print(random_number)
