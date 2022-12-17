# Every KEY in dictionary is UNIQUE

fruits = {"orange": "a sweet orange, citrus fruits",
          "apple": "good for making cider",
          "lemon": "a sour yellow, citrus fruits",
          "grape": "a small sweet fruits, growing in bunches",
          "lime": "a sour green citrus fruits"}
# print(fruits)
# print(fruits["lemon"])
#
# fruits["pear"] = "an odd shaped apple"
# print(fruits["pear"])
#
# fruits["pear"] = "great with tequila"  # Replacing the value of a key
# print(fruits)
#
# del fruits["lemon"]  # Deleting one key and its value in dictionary
# # If we do not enter the specific key then it will delete the entire dictionary
# print(fruits)
# fruits.clear()  # clears the contents of dictionary
# print(fruits)
#
# while True:
#     dict_key = input("Enter the fruits: ")
#     if dict_key.casefold() == "quit":
#         break
#     # 1 st Method to check whether dict has key
#     description = fruits.get(dict_key.casefold(), "We don't have " + dict_key.casefold())
#     print(description)
#     # 2 nd Method
#     if dict_key.casefold() in fruits:
#         description = fruits.get(dict_key.casefold())  # get is used to get value of particular key
#         print(description)
#     else:
#         print(f"We don't have {dict_key}")
#
# #  Iterating over dict
# for fruit in fruits:
#     print(f"{fruit} is {fruits.get(fruit)}")
#
# for val in fruits.values():  # less efficient than by through key
#     print(val)

print(fruits.keys())
print(fruits.values())
print(fruits.items())

# Application of tuple and list in dictionary
f_tuple = tuple(fruits.items())
for snack in f_tuple:
    name, description = snack
    print(description)

