# can be used without parenthesis
t = "a", "b", "c"
print(type(t))
print(t)

# can be used with parenthesis
t = ("a", "b", "c")
print(type(t))
print(t)

welcome = "Welcome to my Nightmare", "Alice Cooper", 1975
bad = "Bad Company", "Bad Company", 1974
budgie = "Nightflight", "Budgie", 1981
imelda = "More Mayhem", "Emilda May", 2011
metallica = "Ride the lightning", "Metallica", 1986

print(metallica)
print(metallica[0])
print(metallica[1])

# metallica[0] = "Master of Puppets"  # tuples are immutable
# hence tuples require less memory than list because it doesn't have methods for muting the data

# ----------------------------------- Unpacking a tuple ---------------------------------------------------------------
print("Unpacking tuple")
x, y, z = 2, 4, 76    # here 2, 4, 76 is a tuple
print(x)
print(y)
print(z)
print()

print("Unpacking tuple")
data_list = [2, 4, 76]  # error because now list is changed this is advantage of tuple
# data_list.append(45)
x, y, z = data_list
print(x)
print(y)
print(z)
print()

# enumerate is application of unpacking a tuple
for index, character in enumerate("abcdef"):
    print(index, character)

# another way of metallica
title, artist, year = metallica
print(title)
print(artist)
print(year)
print()

# -------------------------------------------------- nested tuple and tuple lists ------------------------------------
albums = [
    ("Welcome to my Nightmare", "Alice Cooper", 1975),
    ("Bad Company", "Bad Company", 1974),
    ("Nightflight", "Budgie", 1981),
    ("More Mayhem", "Emilda May", 2011),
    ("Ride the lightning", "Metallica", 1986),
]
for album in albums:
    print("Album: {}, Artist: {}, Year:{} ".format(album[0], album[1], album[2]))
print()

# using unpacking
for name, artist, year in albums:
    print("Album: {}, Artist: {}, Year:{} ".format(name, artist, year))
print()

# indexing in nested lists and tuple
budgie = albums[2][1]
print(budgie)


# Constants
# constants are written in capital letters with underscore for separating
