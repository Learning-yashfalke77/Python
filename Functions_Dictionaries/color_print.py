import colorama

# Some ANSI escape sequences foe colours and effects
BLACK = '\u001b[30m'
RED = '\u001b[31m'
GREEN = '\u001b[32m'
YELLOW = '\u001b[33m'
BLUE = '\u001b[34m'
MAGENTA = '\u001b[35m'
CYAN = '\u001b[36m'
WHITE = '\u001b[37M'
RESET = '\u001b[0m'

BOLD = '\u001b[1m'
UNDERLINE = '\u001b[4m'
REVERSE = '\u001b[7m'


def colour_print(text: str, *effects: str) -> None:
    """
    Print `text` using the ANSI sequences to change colour, etc

    :param text: The text to print
    :param effects: The effect we want. One of the constants defined at the start of this module
    :return:
    """
    effect_string = "".join(effects)
    output_string = "{0}{1}{2}".format(effect_string, text, RESET)
    print(output_string)


colorama.init()
print("This is the default terminal colour")
print(BLACK, "Black")
print(RED, "red")
print(GREEN, "green")
print(YELLOW, "Yellow")
print(BOLD, GREEN, "Green in bold")
print(BOLD, UNDERLINE, RED, "red")
colorama.deinit()
