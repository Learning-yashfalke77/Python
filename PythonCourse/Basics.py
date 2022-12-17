greetings = "Hello"
name = input("Please enter your Name ")
print(greetings + ' ' + name)

splitString = "This String has been\nSplit over\nSeveral\nLines "
print(splitString)

tabbedString = "1\t2\t3\t4"
print(tabbedString)

anotherSplitString = """This String has been
Split Over
Several
Lines """
print(anotherSplitString)

anotherSplitString1 = '''This String has been
Split Over
Several
Lines '''
print(anotherSplitString1)

# -------------------------------------------------------------------------------------------

a = 12
b = 3
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)   # gives Division ans in whole number
print(a % b)
print(a ** 2)   # we are squaring the a variable

parrot = "Norwegian Blue"
print(parrot)
print(parrot[3])  # It reads third position letter excluding last digit
print(parrot[-1])  # It starts read from right hand side
print(parrot[0:6])  # it gives range to print characters in string excluding the last position and including first
# position
print(parrot[:6])
print(parrot[6:])
print(parrot[-4:-2])
print(parrot[0:6:2])  # print value after 2 elements form starting letter
number = "9,223,372,036,854,775,807"
print(number[1::4])
string1 = "He's "
string2 = "probably pinning "
print(string1 + string2)
print("He's " "probably pinning ")
print("Hello " * 5)
today = "Friday"
print("day" in today)  # It is used for searching day substring in String
print("Fri" in today)
print("Thur" in today)
print("parrot" in "fjord")

# ------------------------------ Function Signature ---------------------------
# function signature is the name of the function and parameters that it defines

# here print has 2 arguments which is called as keyword arguments: end and sep
name = "yash"
age = 19
print(name, age, " python ", 2020, sep="@", end=" ")

# -------------------------------------------------------------------------------------------

age = 24
print("My age is " + str(age) + " years")

print("My age is {0} years".format(age))  # Replacement Field
print("""January {0}
February {1}
March {0}
April {2}
May {0}
June {2}                             
July {0}
August {0}
September {2}
October {0}
November {2}
December {0}""".format(31, 28, 30))

print("My age is %d years" % age)
print("My age is %d, %s and %d, %s" % (age, "years", 6, "months"))

for i in range(1, 12):  # here formatting is done by allocating 2 digit space to Given number
    # and 4 digit space for its square and cube
    print("No. %2d squared is %4d and cubed is %4d" % (i, i ** 2, i ** 3))         # String Interpolation
print("PI is approximately %12.50f " % (22 / 7))
# formatting number with 12 digit space and 50 decimal precision

for i in range(1, 12):  # in replacement field {position:width.decimalPointPrecision}
    print("No. {0} squared is {1:2} and cubed is {2:4}".format(i, i ** 2, i ** 3))
    print("No. {0} squared is {1:<2} and cubed is {2:<4}".format(i, i ** 2, i ** 3))
    # for formatting on right hand side
print("PI is approximately {0:12.50} ".format(22 / 7))

for i in range(1, 12):  # this can be done only for numbers in format
    print("No. {:2} squared is {:4} and cubed is {:4}".format(i, i ** 2, i ** 3))


age = 24
print(f"My age is {age} years")             # fString only above 3.6 python
pi = 22 / 7
print(f"The Value of pi is {pi:12.50f}")
