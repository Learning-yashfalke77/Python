# ----------------------------------------------- FOR Loops --------------------------------------------------------
# for loops are generally used with sequences such list, string and ranges
# using range
for x in range(1, 10):  # Gives the range from including 1 to 9 excluding 10
    print(x)

# using strings
# example: checking if the password contains digit
# isnumeric is used to check whether String contains digits
for letter in "yashfalke77":
    if letter.isnumeric():
        print(letter)
    else:
        print("no letters")

# ----------------------------------------------- Ranges ------------------------------------------------------------
# python ranges comes in multiple forms
print(list(range(7)))  # gives you integers from 0 to 6
print(list(range(1, 8)))  # will give you integers from 1 to 7, two parameters are (start , end)
# Third param is called "step" meaning how many to skip.Also, which way to count, up + / down -
print(list(range(1, 10, 2)))
print(list(range(7, 0, -1)))

# --------------------------------------------- CodeAlong - Repeater -------------------------------------------------
times = int(input("How many times i have to tell you :( : "))
for time in range(times):
    print("CLEAN UP YOUR ROOM")

# ------------------------------------------- EXERCISE - Unlucky Nos -----------------------------------------------
# check for even and odd from num 1 to 20
# 4 and 13 should be unlucky no
for no in range(1, 21):
    if no == 4 or no == 13:
        state = "Unlucky"
    elif no % 2 == 0:
        state = "even"
    else:
        state = "odd"
    print(f"{no} is {state} no")

# ------------------------------------------- While Loops ------------------------------------------------------------
# while loop will continue to run while a certain condition is truthy and end when they become falsy
msg = input("Whats the secret password: ")
while msg != "bananas":
    print("WRONG")
    msg = input("Whats the secret password: ")
print("CORRECT!")

#  Emoji codeAlong
for num in range(1, 11):
    print("\U0001f600" * num)

times = 1
while times <= 11:
    print("\U0001f600" * times)
    times += 1

for x in range(3):
    for num in range(1, 11):
        print("\U0001f600" * num)

# Stop copying me codeAlong
msg = input("Say Something: ")
while msg != "stop copying me":
    msg = input(f"{msg}\n")
print("Ok fine you win")

# -------------------------------------------- Break Keyword -------------------------------------------------------
while True:
    command = input("Type 'exit' to exit: ")
    if command == "exit":
        break
