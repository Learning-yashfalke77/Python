from random import randint

print("""...rock...
...paper...
...scissors...
""")

# ----------------------------------------- Using 2 Players -----------------------------------------------------------
# player1 = input("Player1, make your move: ")
# print("***** NO CHEATING ******\n\n" * 20)
# player2 = input("Player2, make your move: ")
#
# if player1 == player2:
#     print("Its an Tie")
# elif player1 == "rock":
#     if player2 == "scissor":
#         print("player 1 wins")
#     elif player2 == "paper":
#         print("player 2 wins")
# elif player1 == "paper":
#     if player2 == "scissor":
#         print("player 2 wins")
#     elif player2 == "rock":
#         print("player 1 wins")
# elif player1 == "scissor":
#     if player2 == "rock":
#         print("player 2 wins")
#     elif player2 == "paper":
#         print("player 1 wins")
# else:
#     print("Something went wrong! ")
# ----------------------------------------- Using 1 player and 2nd is AI ---------------------------------------------
player = input("Player1, make your move: ").casefold()
entities = ["rock", "paper", "scissor"]
num = randint(0, 2)
computer = entities[num]
print(f"computer chose {computer} ")

if player == computer:
    print("Its an Tie")
elif player == "rock":
    if computer == "scissor":
        print("player wins")
    elif computer == "paper":
        print("computer wins")
elif player == "paper":
    if computer == "scissor":
        print("computer wins")
    elif computer == "rock":
        print("player wins")
elif player == "scissor":
    if computer == "rock":
        print("computer wins")
    elif computer == "paper":
        print("player wins")
else:
    print("Something went wrong! ")
