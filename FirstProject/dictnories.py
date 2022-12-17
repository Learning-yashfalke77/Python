# A data structure that consists of key value pairs
# We use keys to describe our data and values to represent our data
cat = {
    "name": "blue",
    "age": 3.5,
    "isCute": True,
}
print(cat)

# Another way of defining dictionaries
cat2 = dict(name="kitty", age=0.5)
print(cat2)

# ----------------------------------- Accessing another values -------------------------------------------------------
print(cat["age"])

# ------------------------------------ Iterating over dictionaries ---------------------------------------------------
print(cat.values())  # returns a iterable values
for value in cat.values():
    print(value)

print(cat.keys())  # returns an iterable keys
for keys in cat.keys():
    print(keys)

print(cat.items())  # returns an iterable key value pairs
for k, v in cat.items():
    print(f"{k}: {v}")

# ------------------------------ To check whether a key is present in dictionary-------------------------------------
print("name" in cat)
print("yoo" in cat)

# ------------------------------ To check whether a value is present in dictionary-------------------------------------
print("blue" in cat.values())
print("yash" in cat.values())

# ---------------------------------------------- built in functions -------------------------------------------------

instructor = {
    "name": "Colt",
    "owns_dog": True,
    "num_courses": 4,
    "favourite_languages": "python",
    "is_hilarious": True,
    44: "my favourite number",
}

# 1) copy: make a copy of dictionary
instructor1 = instructor.copy()
print(instructor1 is instructor)  # they are not equal
print(instructor1)

# 2) clear: clear all the keys and values in dictionary
instructor1.clear()
print(instructor1)

# 3) fromKeys: creates key value pairs from a comma separated values
new_user = {}.fromkeys(['name', 'email', 'score', 'profile bio'], 'unknown')
print(new_user)

# 4) get: Retrieves a key in an object and returns none instead of keyError if the  key does not exist
print(instructor.get("name"))
print(instructor.get("email"))

# 5) pop: Takes a single argument corresponding to a key and remove key value pairs from dictionary
# Returns the value corresponding to the key that was removed
print(instructor.pop("owns_dog"))
print(instructor)

# 6) popitem: removes a random key in dictionary
print(instructor.popitem())
print(instructor)

# 7) update: update the keys and values in dictionary with another set of key value pairs
person = {"city": "mumbai"}
person.update(instructor)
print(person)

# ----------------------------------------- Dictionary Comprehension ---------------------------------------------------
yelling_instructor = {str(k).upper(): str(v).upper() for k, v in instructor.items()}
print(yelling_instructor)

print({num: ("even" if num % 2 == 0 else "odd") for num in range(1, 100)})
