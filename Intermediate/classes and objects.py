# oop is method of programming that attempts to model some process or things in the world as classes and objects
# class: class is a blueprint for objects, Classes contains methods (functions) and attributes (similar to keys in dict)
# instance: objects that are constructed from a class blueprint that contains their class methods and properties
# help(int)   # to get docs
# Encapsulation:The grouping of public & private attributes & method into programmatic class making abstraction possible

# ----------------------------------------------- defining class------------------------------------------------------
# class User:
#     pass
#
#
# user1 = User()
# user2 = User()
# print(user1)

# ---------------------------------------------- __init__ method ----------------------------------------------------
# class in python have a special __init__ method, which gets called everytime you create instance of class (instantiate)
# init method is used to initialize the data that it has

# -------------------------------------------------- self ------------------------------------------------------------
# the self keyword refers to the current class instance
# self always the first parameter to the __init__ and methods and properties on class

# class User:
#     def __init__(self, first, last, age):
#         self.first = first
#         self.last = last
#         self.age = age
#
#
# user1 = User("Joe", "Smith", 68)
# user2 = User("blanca", "lopez", 41)
# print(user1.first, user1.last, user1.age)
# print(user2.first, user2.last, user2.age)


# --------------------------- underscore dunder methods, name mangling, and more --------------------------------------
# _name: convention followed by developers that this is a private method or private property, intend for internal use
# __name (name mangling): python will change the name , so that we can't access it
# __name__ (Dunder methods) : these are special things that python looks for, don't define on your own

# class Person:
#     def __init__(self):
#         self.name = "yash"
#         self._secret = "this is a secret"
#         self.__msg = "this is my message"
#
#
# person1 = Person()
# print(person1.name)
# print(person1._secret)
# print(person1._Person__msg)  # but not as person1.__msg


# ------------------------------ instance attributes and methods ----------------------------------------------------
# attributes and methods are defined on each instance
# class User:
#     def __init__(self, first, last, age):
#         self.first = first
#         self.last = last
#         self.age = age
#
#     def full_name(self):
#         return f"{self.first} {self.last}"
#
#     def initials(self):
#         return f"{self.first[0]}.{self.last[0]}"
#
#     def likes(self, things):
#         return f"{self.first} likes {things}"
#
#     def is_senior(self):
#         return self.age > 65
#
#     def birthday(self):
#         self.age += 1
#         return f"happy {self.age}th birthday, dear {self.first}"
#
#
# user1 = User("Joe", "Smith", 68)
# user2 = User("blanca", "lopez", 41)
# print(user1.full_name())
# print(user2.initials())
# print(user1.likes("chips"))
# print(user2.is_senior())
# print(user1.birthday())

# ----------------------------- class attributes and methods ------------------------------------------------------
# we can also define attributes directly on a class that are shared by all instances of a class and class itself
# class User:
#     # class variable
#     active_users = 0
#
#     # class method
#     @classmethod
#     def display_active_users(cls):
#         return f"there are currently {cls.active_users} users"
#
#     def __init__(self, first, last, age):
#         self.first = first
#         self.last = last
#         self.age = age
#         User.active_users += 1
#
#     def full_name(self):
#         return f"{self.first} {self.last}"
#
#     def logout(self):
#         User.active_users -= 1
#         return f"{self.first} has been logged out :("
#
#     def initials(self):
#         return f"{self.first[0]}.{self.last[0]}"
#
#     def likes(self, things):
#         return f"{self.first} likes {things}"
#
#     def is_senior(self):
#         return self.age > 65
#
#     def birthday(self):
#         self.age += 1
#         return f"happy {self.age}th birthday, dear {self.first}"
#
#
# print(User.active_users)
# user1 = User("Joe", "Smith", 68)
# user2 = User("blanca", "lopez", 41)
# print(User.active_users)
# user2.logout()
# print(User.active_users)
# print(User.display_active_users())
#
#
# class Pet:
#     allowed_pet = ['cat', 'dog', 'fish', 'rat']
#
#     def __init__(self, name, species):
#         if species not in Pet.allowed_pet:
#             raise ValueError(f"You cant have a {species} pet")
#         self.name = name
#         self.species = species
#
#     def set_species(self, species):
#         if species not in Pet.allowed_pet:
#             raise ValueError(f"You cant have a {species} pet")
#         self.species = species
#
#
# cat = Pet("Blue", "cat")
# dog = Pet("Wyatt", "dog")
# tony = Pet("tony", "tiger")


# --------------------------------- String representation example ------------------------------------------------
# the __repr__ method is one of the several ways to provide a nicer string representation

class Users:
    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self.age = age

    def __repr__(self):
        return f"{self.first} is {self.age}"

    def full_name(self):
        return f"{self.first} {self.last}"

    def initials(self):
        return f"{self.first[0]}.{self.last[0]}"

    def likes(self, things):
        return f"{self.first} likes {things}"

    def is_senior(self):
        return self.age > 65

    def birthday(self):
        self.age += 1
        return f"happy {self.age}th birthday, dear {self.first}"


user2 = Users("blanca", "lopez", 41)
print(user2)
