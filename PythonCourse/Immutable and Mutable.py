# --------------------------- Immutable -----------------------------------------------
# Immutable object cant be changed, you can create a new object and use same variable name for it
result = True
another_result = True     # here result and another_RESULT HAVE SAME VALUE HENCE SAME ID (refers to same object)
print(id(result))
print(id(another_result))

result = False
print(id(result))
print()
# Here the value has not changed, but a new object is created and the result is bound towards new object
# Hence int, float, String, frozenset, tuple, bytes, boolean are immutable

results = "correct"
another_results = results
print(id(results))
print(id(another_results))

results += "ish"  # Augmented Assignment
print(id(result))
print(id(another_results))
print()


# ------------------------------- Mutable ------------------------------------------------
# Whose values of objects can be changed, without being destroyed or recreated
# Mutable objects are list, dict, set, bytearray

shopping_lists = ["milk",
                  "pasta",
                  "eggs",
                  "bread",
                  "rice"
                  ]
another_shopping_lists = shopping_lists
print(id(shopping_lists))
print(id(another_shopping_lists))

another_shopping_lists += ["carrot"]
print(another_shopping_lists)
print(id(another_shopping_lists))    # Since id number is same hence, they are mutable

