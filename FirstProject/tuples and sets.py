# tuple is an ordered collection of items
# same as list, but it is an immutable data type
# tuples are faster than lists
alphabets = ('a', 'b', 'c', 'd')
print(alphabets)
# alphabet[1] = c    # will give error because it is an immutable
# it is used in .items or .keys or .values in dictionary

# ----------------------------------- accessing tuple values -----------------------------------------------------
print(alphabets[0])

# ---------------------------- tuples used as a keys in dictionary -------------------------------------------------
locations = {
    (35.6895, 39.6917): "Tokyo office",
    (40.7218, 74.0060): "New York office",
    (37.7749, 122.4194): "San Francisco office"
}

print(locations[(37.7749, 122.4194)])

# cannot use list as keys in dictionary

# --------------------------------- Iterating over tuples ------------------------------------------------------------
for alphabet in alphabets:
    print(alphabet)

# ------------------------------------ tuple methods ----------------------------------------------------------------
# 1) counts: returns a number of times a value appears in tuple
x = (1, 2, 3, 2, 3, 5, 3)
print(x.count(1))

# 2) index : Returns an index at which a value is found in tuple
print(x.index(3))

# ______________________________________________ SETS _________________________________________________________________
# Sets is a collection of data that do not have duplicate values and there is nu order
# cannot access the data by index because there is no order
s = {1, 3, 5}
print(s, type(s))

s1 = set({1, 2, 3, 4, 5, 2, 4, 5, 2})
print(s1)

# ------------------------------- accessing value in set ----------------------------------------------------------
for ss in s:
    print(ss)

# ------------------------------------------ set methods ----------------------------------------------------------
# 1) add: Adds elements to set, if element is already there, it doesn't change
s.add(6)
print(s)

# 2) remove: remove an elements from set
s.remove(6)
print(s)
# discard method same as remove but does not throw error if the element ids not present in set

# 3) copy: copies the set
print(s.copy())

# 4) clear: clears the set

# 5) set math
maths_students = {"Mathew", "Helen", "Prashant", "James", "Aparna"}
biology_students = {"Jane", "Mathew", "Charlotte", "Mesut", "Oliver", "James"}

# set unions
print(maths_students | biology_students)

# set intersections
print(maths_students & biology_students)

# -------------------------------------- Set Comprehensions --------------------------------------------------------
print({x ** 2 for x in range(1, 10)})
print({char.upper() for char in 'hello'})