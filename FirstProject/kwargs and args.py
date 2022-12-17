# ------------------------------------------- * args ----------------------------------------------------------------
#  a special operator passed to function
# gather remaining arguments as a tuple
# this is just a parameter you can call it whatever you want
def sum_all_nums(*args):
    total = 0
    for num in args:
        total += num
    return total


print(sum_all_nums(1, 2, 3))


# ------------------------------------**kwargs (keyword arguments) ----------------------------------------------------
#  a special operator passed to function
# gather remaining arguments as a dictionary
# this is just a parameter you can call it whatever you want

def fav_colors(**kwargs):
    for person, color in kwargs.items():
        print(f"{person}'s favourite color is {color}")


fav_colors(colt="purple", ruby="red", ethal="teal")


# ------------------------------------------- Parameters Ordering -----------------------------------------------------
# 1) parameters, 2) *args, 3) default parameters, 4) **kwargs
def display_info(a, b, *args, instructor="colt", **kwargs):
    return [a, b, args, instructor, kwargs]


print(display_info(1, 2, 3, last_name="steele", job="instructor"))

# ------------------------------------------ tuple unpacking-------------------------------------------------------
nums = [1, 2, 3, 4, 5, 6]
print(sum_all_nums(*nums))
print(*nums)


# ------------------------------------------ dictionary unpacking ---------------------------------------------------
def display_names(first, second):
    print(f"{first} says hello to {second}")


names = {"first": "colt", "second": "steele"}
display_names(**names)
print({**names})