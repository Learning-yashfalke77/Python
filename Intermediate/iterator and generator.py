# "Hello is an iterable , but it is not iterator "
# iter("Hello") returns an iterator
name = "opera"
it = iter(name)
print(next(it))
print(next(it))


# Iter gives an iterator object
# when next called on iterator , the iterator returns a next item, keeps doing until it raises stop Iteration error

# defining custom for loop
def my_for(iterable, func):
    iterator = iter(iterable)
    while True:
        try:
            thing = next(iterator)
        except StopIteration:
            break
        else:
            func(thing)


my_for("Hello", print)


class Counter:
    def __init__(self, low, high):
        self.current = low
        self.high = high

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < self.high:
            num = self.current
            self.current += 1
            return num
        raise StopIteration


for x in Counter(10, 20):
    print(x)


# ----------------------------------------- generators -------------------------------------------------------------
# generators are iterators
# generators can be created with generator functions
# Generator function use the yields' keyword
# generator functions returns a generator
# whenever you write yield it will return generator and stops until the next time it is not called

def count_up_to(maxi):
    count = 1
    while count <= maxi:
        yield count
        count += 1


gen = count_up_to(3)
print(gen)
print(next(gen))
print(next(gen))
print(next(gen))
