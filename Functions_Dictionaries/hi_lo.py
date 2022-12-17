# low = 1
# high = 1000
#
#
# def guess_binary(answer, lows, highs):
#     guesses = 1
#     while True:
#         guess = lows + (highs - lows) // 2
#         if guess < answer:
#             lows = guess + 1
#         elif guess > answer:
#             highs = guess - 1
#         elif guess == answer:
#             return guesses
#
#         guesses += 1
#
#
# for number in range(low, high + 1):
#     number_of_guesses = guess_binary(number, low, high)
#     print("{} guessed in {}".format(number, number_of_guesses))

# -------------------- * Arguments -----------------------------------
# * arguments is used to unpacked any sequences
# number = (1, 2, 3, 4, 5, 6)
# print(number, sep=";")
# print(*number, sep=";")
# print(1, 2, 3, 4, 5, 6, sep=";")
#
#
# def star_args(*args):  # unpacking the tuple
#     print(args)
#     for x in args:
#         print(x)
#
#
# star_args(1, 2, 3, 4, 5, 6)  # here is unpacked tuple passed as an argument but python packs it as tuple
# # Hre we can pass any no of arguments like print function
# print()
# star_args()  # can also pass zero argument show blank tuple

# ----------------------------  priority/ order of parameters writing in fn --------------------


def fun(p1, p2, *args, k, **kwargs):
    print("positional-or-keyword arguments:...{} {}".format(p1, p2))
    print("var-positional arguments:...........{}".format(args))
    print("keyword arguments:..................{}".format(k))
    print("var-keyword arguments...............{}".format(kwargs))


fun(1, 2, 3, 4, 5, k=6, key1=7, key2=8, key3=9)
