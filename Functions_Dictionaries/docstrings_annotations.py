# DOCSTRING is used for documentation
# DOCSTRING IS THE TRIPLE CODES AT STARTING AND ENDING
# It is used at start of particular function and class
# TODO: INFO DOCSTRING https://www.python.org/dev/peps/pep-0257/

# function annotations :
# They make it clearer what kind of value your function can accept and what they return


# ---------------------- EXAMPLE 1 --------------------------------------
def get_integer(prompt: str) -> int:  # annotations
    """
    Get an Integer from Standard Input (stdin)

    The function will continue looping and prompting
    the user, until a valid `int` is entered.

    :param prompt: The String that user will see, when they're prompted to
        enter the value
    :return: The integer that the user enters
    """
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

print(get_integer.__doc__)  # prints the documentation of function
help(get_integer)  # prints the documentation of function


# ----------------------- Example 2: Fibonacci -------------------------------


def fibonacci(n: int) -> None:  # annotations
    """
    Get an Integer from Standard Input (stdin)
    Return the `n` th Fibonacci number for `n` Positive number

    :param n: n is positive number which should be entered by user
    :return: the Fibonacci series till the `n` given number
    """
    if 0 <= n <= 1:
        print(n)
    print("0\n1")
    if n < 0:
        raise ValueError("Expected positive number but got negative no")
    n_minus1, n_minus2, result = 1, 0, None
    for i in range(n - 1):
        result = n_minus1 + n_minus2
        print(result)
        n_minus2 = n_minus1
        n_minus1 = result


fibonacci(5)


# -------------------- Annotations and hints (Palindrome) ----------------------


def is_palindrome(string: str) -> bool:  # annotations
    """
    Check if a string is palindrome
    a Palindrome is a string that reads the same forward as well as backwards

    :param string: The string to check
    :return: True if string is Palindrome, otherwise False
    """
    return string.casefold()[::-1] == string.casefold()


sentence = input("Enter the word to check ")
if is_palindrome(sentence):
    print("{} is palindrome".format(sentence))
else:
    print("{} is not palindrome".format(sentence))


#  ---------------- Multiplication two numbers ------------------------------


def multiply(x: float, y: float) -> float:  # formal parameters
    """
    Multiply 2 given number from Standard Input (stdin).

    :param x: The first number to multiply.
    :param y: The  number to multiply x by.
    :return: the product of x and y.
    """
    result = x * y
    return result


print(multiply(3, 2))


# # ------------------- Annotations for default value --------------------------


def banner_text(text: str = " ", screen_width: int = 80) -> None:  # DEFAULT ARGUMENT and positional arguments
    """
    Prints beautiful starting intro for your app


    :param text: one line Message that you want to print
    :param screen_width: width of the screen
    :raise raise exception when the length of text is too large as compared to screen width
    """
    if len(text) > screen_width - 4:
        raise ValueError("String {0} is larger than the expected width {1}".format(text, screen_width))
    if text == "*":
        print("*" * screen_width)
    else:
        centred_text = text.center(screen_width - 4)
        output_string = "**{0}**".format(centred_text)
        print(output_string)


banner_text("*", 66)  # positional arguments
banner_text("Always look on the bright side of life....", 66)  # positional arguments
banner_text("If life seems jolly rotten,", 66)  # positional arguments
banner_text("There's something you've forgotten!", 66)  # positional arguments
banner_text("And that's to laugh and smile and dance and sing,")  # positional arguments
banner_text(screen_width=66)  # keyword arguments
banner_text("When you are feeling in the dumps", 66)  # positional arguments
banner_text("Don't be silly chumps,", 66)  # positional arguments
banner_text("*", 66)  # positional arguments
