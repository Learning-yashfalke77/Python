# join does the iteration for us without using the for loop
# we give it an iterable and it joins all the items in a iterable
# it is used for string classes only
# At starting we should mention the separator that join should use
# all the items in the iterable must be string to use join method and not works on int etc

flowers = [
    "Daffodil",
    "Evening Primrose",
    "Hydrangea",
    "Iris",
    "Lavender",
    "Sunflower",
    "Tiger Lily",
]

for flower in flowers:
    print(flower)

separator = ", "
output = separator.join(flowers)
print(output)

print(" | ".join(flowers))

# --------------------------------------------------------------------------------------------
# split
# It takes the input as a string and returns the list containing items in string separated by separator
# note separator can be given in arguments, if no arguments given use whitespace as a separator

panagram = "The quick brown box jumps over the lazy dog"
print(panagram.split())

#               join and split

generated_list = ['9', ' ',
                  '2', '2', '3', ' ',
                  '3', '7', '2', ' ',
                  '0', '3', '6', ' ',
                  '8', '5', '4', ' ',
                  '7', '7', '5', ' ',
                  '8', '0', '7'
                  ]
values = ''.join(generated_list)  # convert list to string
print(values)

list_without_space = values.split()  # convert list to strings
print(list_without_space)

# converting list of strings into list of ints
for index in range(len(list_without_space)):
    list_without_space[index] = int(list_without_space[index])
print(list_without_space)

# or creating new list
new_list = []
for value in list_without_space:
    new_list.append(int(value))
print(new_list)
