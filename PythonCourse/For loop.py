# For loop is generally used when you know in advance, how many times the loop will execute
parrot = "Norwegian Blue"
for character in parrot:
    print(character)

number = input("Enter the number series, with any of the separators you like: ")
sep = ""
for char in number:
    if not char.isnumeric():    # isnumeric is used to check whether String contains digits
        sep = sep + char
print(sep)

# --------------------------- Ranges --------------------------------------
for i in range(1, 20):                   # Gives the range from including 1 to 19 excluding 20
    print(f"i is now in {i}")
print()

for i in range(10):                     # start printing from 0 by default
    print(f"i is now in {i}")
print()

for i in range(0, 10, 2):              # start printing by the 2 step
    print(f"i is now in {i}")
print()

for i in range(10, 0, -1):             # to go in reverse order always mention yhe step number in negative
    print(f"i is now in {i}")

age = int(input("Enter the age dear: "))
if age in range(16, 66):               # Application of range in if statement
    print("Have a god day at work")
else:
    print("Enjoy your free time ")

# --------------------- Nested for loops ---------------------------
for i in range(1, 13):
    for j in range(1, 13):
        print("{0} * {1} = {2}".format(i, j, i * j))
    print("-" * 20)

# ------------------------ List -----------------------------------------------
# a list in a python is an ordered sequence of values enclose in a square brackets
# Application of for loop in list
shoppingList = ["Milk", "Pasta", "Butter", "Egg"]
for item in shoppingList:
    if item != "Egg":
        print("Buy " + item)

for item in shoppingList:          # Using continue
    if item == "Egg":
        continue
    print("Buy " + item)

# ----------- Using break --------------------------------
shoppingList = ["milk", "pasta", "butter", "egg"]
item = input("Enter the item to search to buy: ")
found_at = None

for index in range(len(shoppingList)):
    if item.casefold() == shoppingList[index]:
        found_at = index
        break

# Alternate code for this for
if item in shoppingList:
    found_at = shoppingList.index(item)

if found_at is None:
    print("The {} is not present in your shopping list".format(item))
else:
    print("{0} is found at {1}".format(item, found_at))
