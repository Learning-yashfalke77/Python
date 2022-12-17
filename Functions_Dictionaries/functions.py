# Function is used to avoid duplication of code and you can use again and again
# parameters in function are of two  type i.e POSITIONAL and KEYWORD parameters
def multiply(x, y):  # formal parameters
    result = x * y
    return result


answer = multiply(10, 20)  # two blank line should be there after the function
print(answer)

forty_two = multiply(7, 6)  # actual parameters
print(forty_two)

for number in range(1, 6):
    print(f"two times: {multiply(2, number)}")
print()


#  -------------------- palindrome -------------------------------------------


def is_palindrome(string):
    return string.casefold()[::-1] == string.casefold()


def palindrome_sentence(sentences):  # checking for sentences
    string = ""
    for char in sentences:
        if char.isalnum():
            string += char
    # return string.casefold()[::-1] == string.casefold()
    return is_palindrome(string)


# TODO: String in build methods https://docs.python.org/3/library/stdtypes.html#string-methods

sentence = input("Please enter the word: ")
if palindrome_sentence(sentence):
    print("{} is palindrome".format(sentence))
else:
    print("{} is not palindrome".format(sentence))


# -------------------- Guessing Game -------------------------------------------


def get_integer(prompt):
    while True:
        temp = input(prompt)
        if temp.isnumeric():
            return int(temp)
        else:
            print("Enter the numeric value")


import random

answer = random.randint(1, 10)
print("Please enter the number between 1 to 100")
guess = get_integer(": ")
while guess != answer:
    if guess == 0:
        print("Exited the Game")
        break
    else:
        if guess < answer:
            print("Please guess higher: ")
            guess = get_integer(": ")
        else:
            print("Please guess lower: ")
            guess = get_integer(": ")
if guess == answer:
    print("Voila, you had guessed the number correctly")


# ----------------------------------------------------------------
# formatting console stsrt


def banner_text(text=" ", screen_width=80):   # DEFAULT ARGUMENT and positional arguments
    if len(text) > screen_width - 4:
        # print("EEK!")
        # print("THE TEXT IS TOO LONG TO FIT IN THE SPECIFIED WIDTH")
        raise ValueError("String {0} is larger than the expected width {1}".format(text, screen_width))
        # here value error because exception was caused by the value of text
    # TODO: types of exception https://docs.python.org/3/library/exceptions.html
    if text == "*":
        print("*" * screen_width)
    else:
        centred_text = text.center(screen_width - 4)
        output_string = "**{0}**".format(centred_text)
        print(output_string)


banner_text("*", 66)
banner_text("Always look on the bright side of life....", 66)
banner_text("If life seems jolly rotten,", 66)
banner_text("There's something you've forgotten!", 66)
banner_text("And that's to laugh and smile and dance and sing,")
banner_text(screen_width=66)  # keyword arguments
banner_text("When you are feeling in the dumps", 66)
banner_text("Don't be silly chumps,", 66)
banner_text("*", 66)
