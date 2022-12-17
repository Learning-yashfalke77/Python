# ------------------------------------ property in classes (getters and setters ) ------------------------------------
class Human:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if value >= 0:
            self._age = value
        else:
            self._age = 0


yash = Human("yash falke", 20)
# accessing a getter
print(yash.age)
# accessing a setter
yash.age = 22
print(yash.age)


# --------------------------------------------------- inheritance ---------------------------------------------------
# a key feature of OOP is ability to define a class which inherits from another class (a base from parent class)
# In python , inheritance works by passing the parent class as an argument to the definition of child class

# class Animal:
#     cool = True
#
#     def make_sounds(self, sound):
#         print(f"This animal says {sound}")
#         return self
#
#
# class Cat(Animal):
#     pass
#
#
# blue = Cat()
# blue.make_sounds("Meow Meow")
# print(isinstance(blue, Animal))

# ----------------------------------------------- super keyword -----------------------------------------------------
class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def __repr__(self):
        return f"{self.name} is a {self.species}"

    def make_sounds(self, sound):
        print(f"This animal says {sound}")
        return self


class Cat(Animal):
    def __init__(self, name, breed, toy):
        super().__init__(name, species="cat")
        self.breed = breed
        self.toy = toy

    def play(self):
        print(f"{self.name} plays with {self.toy}")


blue = Cat("Blue", "Scottish Fold", "string")
print(blue)
blue.make_sounds("Meow Meow")
blue.play()


# ----------------------------------------------- Multiple inheritance ------------------------------------------------
class Aquatic:
    def __init__(self, name):
        print("Aquatic init")
        self.name = name

    def swim(self):
        return f"{self.name} is swimming"

    def greet(self):
        return f"I am {self.name} of the sea"


class Ambulatory:
    def __init__(self, name):
        print("Ambulatory init")
        self.name = name

    def walking(self):
        return f"{self.name} is walking"

    def greet(self):
        return f"I am {self.name} of the land"


class Penguin(Aquatic, Ambulatory):
    def __init__(self, name):
        print("Penguin init")
        super().__init__(name=name)
        Ambulatory.__init__(self, name=name)


jaws = Aquatic("Jaws")
lassie = Ambulatory("Lassie")
captain_cook = Penguin("Captain Cook")
print(captain_cook.swim())
print(captain_cook.walking())
print(captain_cook.greet())

# -------------------------------- Method Resolution Order ------------------------------------------------------------
# Whenever you create a class, Python sets an MRO , for the class , which is the order in which python will look for
# methods on instances for class
# You can programmatically reference MRO in three ways:
# 1) __mro__ attribute on the class
# 2) use mro() method on the class
# 3) use the built-in help(cls) method

print(Penguin.__mro__)
print(Penguin.mro())
print(help(Penguin))

# --------------------------------------------- Polymorphism ---------------------------------------------------------
# an object can take many(poly) forms(morph)
# applications are:
# 1) The same class method works in similar way for different class
# 2) The same operation works for different kind of objects

