def square(num):
    return num * num


print(square(3))
square2 = lambda num: print(num * num)
square2(9)

# ------------------------------------- built in functions ----------------------------------------------------------
# 1) map
# map returns a map object
nums = [2, 4, 6, 8]
doubles = list(map(lambda x: x * 2, nums))
print(doubles)

peoples = ["Darcy", "Christina", "Dana", "Anabel"]
upper_people = list(map(lambda people: people.upper(), peoples))
print(upper_people)

# 2) filter
# filter returns a filter object
names = ["austin", "penny", "Anthony", "angel", "billy"]
names_a = list(filter(lambda name: name[0].casefold() == 'a', names))
print(names_a)

users = [
    {"username": "samuel", "tweet": ["I love cake", "I love pie"]},
    {"username": "katie", "tweet": ["I love my cat"]},
    {"username": "jeff", "tweet": []},
    {"username": "bob123", "tweet": []},
    {"username": "doggo_luvr", "tweet": ["dogs are the best"]},
    {"username": "guitar_gal", "tweet": []},
]

inactive_users = list(filter(lambda u: not u["tweet"], users))
print(inactive_users)

# ----- combining filter and map
inactive_username = list(map(lambda user: user["username"].upper(), filter(lambda u: not u["tweet"], users)))
print(inactive_username)

# ------ using list comprehensions
# use list comprehensions over map filter built-in functions
print([user["username"].upper() for user in users if not user["tweet"]])

# -------------------------------------------------- ALL -------------------------------------------------------------
# Returns true if all the elements of the iterable are truthy
print(all([0, 1, 2, 3, 4]))
print(all([nums[0] == "a" for name in names]))

# ---------------------------------------------------- ANY--------------------------------------------------------
# Returns true if all the elements of the iterable are truthy
nums = [2, 60, 18, 26, 21]
print(any([num % 2 == 0 for num in nums]))

# ---------------------------------------------------- sorted ---------------------------------------------------------
# returns a copy
print(sorted([6, 1, 8, 2]))
print(sorted([6, 1, 8, 2], reverse=True))
# we can pass also tuple
print(sorted((6, 1, 8, 2)))
# sort the tweets by username
print(sorted(users, key=lambda user: user["username"]))
print(sorted(users, key=lambda user: len(user["tweet"])))

# ----------------------------------------------- max min ------------------------------------------------------------
# returns the largest iterable or the largest of two or more arguments
print(max(3, 67, 99))
print(max(nums))

# getting the max length of the name
# generator expressions
print(max(len(name) for name in names))
print(min(names, key=lambda n: len(n)))

songs = [
    {"title": "happy birthday", "playcount": 1},
    {"title": "survive", "playcount": 6},
    {"title": "YMCA", "playcount": 99},
    {"title": "Toxic", "playcount": 31},
]
print(max(songs, key=lambda s: s['playcount']))

# ----------------------------------------------- reversed ----------------------------------------------------------
# returns the reverse of iterable
# returns a new copy
nuns = [1, 2, 3, 4]
reversed(nuns)  # returns a reversed object
print(list(reversed(nuns)))

# ---------------------------------------------- abs -----------------------------------------------------------------
# returns a absolute value, the argument may be an integer or floating point number
print(abs(-5))
print(abs(5))

# fab is floating point absolute number
import math

math.fabs(4)

# --------------------------------------------------- sum ------------------------------------------------------------
print(sum([1, 2, 3]))
print(sum([1, 2, 3], 10))  # 10 is starting value of total

# --------------------------------------------------------------- round ----------------------------------------------
print(round(10.2))
print(round(3.14175, 3))

# -------------------------------------------------- zip -------------------------------------------------------------
first_zip = zip([1, 2, 3], [4, 5, 6])
print(list(first_zip))
print(dict(first_zip))