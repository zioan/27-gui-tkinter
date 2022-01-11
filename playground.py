# *args
def add(*args):
    return sum(args)

# or


def add(*args):
    print(type(args))  # return a tuple
    print(args[0])
    total = 0
    for n in args:
        total += n
    return total


print(add(1, 2, 3, 5, 27))


# **kwargs
def calculate(n, **kwargs):
    print(kwargs)  # return a dictionary
    # for (key, value) in kwargs.items():
    #     print(key)
    #     print(value)
    print(kwargs["add"])  # 3
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)  # (2 + 3)* 5 = 25


calculate(2, add=3, multiply=5)


#

class Car:
    def __init__(self, **kw):
        self.make = kw["make"]
        self.model = kw["model"]

        # .get() this will return None instead of an error if the argument value is not provided
        # .get() is a better way to construct class params
        self.color = kw.get("color")
        self.seats = kw.get("seats")
        self.engine = kw.get("engine")


my_car = Car(make="Nissan", model="GTR")

print(my_car.model)
print(my_car.make)
print(my_car.color)
