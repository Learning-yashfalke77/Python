# --------------------------------------- built in modules ----------------------------------------------------------
# 1) import random
# # we can give alias name to module by using as
# 2) import random as omg_so_random
# # we can also import a part of the module
from random import choice, shuffle  # 3)

# # we can also import all
# 4) from random import *
# we can also rename the selective imported function
# 5) from random import choice as gimme_one, shuffle as mix_up_fruits
print(choice(["apple", "banana", "cherry", "durian"]))
shuffle(["apple", "banana", "cherry", "durian"])

# TODO: for more packages visit - https://docs.python.org/3/py-modindex.html

# ----------------------------------------- 2) custom module -----------------------------------------------------
import bananas
import apples

print(bananas.dip_in_chocolate())
print(apples.offer())

# ------------------------------------------ 3) external modules ------------------------------------------------
# pypi the python packages index
# it has all info of all external modules
# TODO: for all external packages visit here - https://pypi.org/
# you can download external modules using pip
# TODO: python -m pip install <package-name>

from termcolor import colored

# print(help(termcolor))
text = colored("hello beta", color="magenta", on_color="on_cyan", attrs=["blink"])
print(text)

# ---------------  ascii art exercise
# python -m pip install pyfiglet
import pyfiglet
msg = input("What would you like to print? ")
color = input("Enter the color ")

valid_colors = ("red", "green", "yellow", "blue", "magenta", "cyan", "white")
if color not in valid_colors:
    color = "magenta"

ascii_art = pyfiglet.figlet_format(msg)
colored_ascii = colored(ascii_art, color=color)
print(colored_ascii)
