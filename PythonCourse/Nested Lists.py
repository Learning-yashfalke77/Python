even = [2, 4, 6, 8]
odd = [1, 3, 5, 7]

numbers = [even, odd]  # creates nested list

# print a list inside list and its values
for number_list in numbers:
    print(number_list)
    for values in number_list:
        print(values)

# always use comma in the end item also when closing bracket is on the next line

menu = [
    ["eggs", "bacon"],
    ["eggs", "sausage", "bacon"],
    ["eggs", "spam"],
    ["eggs", "spam", "bacon"],
    ["eggs", "sausage", "bacon", "spam"],
    ["spam", "sausage", "spam", "bacon", "spam", "tomato", "spam"],
    ["spam", "eggs", "spam", "spam", "bacon", "spam"],
]
#
# # processing the lists
# for meal in menu:
#     if "spam" not in meal:
#         print(meal)
#
#         for items in meal:
#             print(items)
#         print()
#     else:
#         print(f"{meal} contains spam score of {meal.count('spam')}")
# print()

# Challenge: remove the spam from all these lists
for meal in menu:
    for index in range(len(meal) - 1, -1, -1):
        if meal[index] == "spam":
            del meal[index]
    print(", ".join(meal))  # using join to remove brackets

# ------------------------------ Function Signature ---------------------------
# function signature is the name of the function and parameters that it defines

# here print has 2 arguments which is called as keyword arguments: end and sep
name = "yash"
age = 19
print(name, age, " python ", 2020, sep="@", end=" ")
