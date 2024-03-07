# *args
def add(*args):
    print(sum(args))


add(1, 2, 1, 1, 1)


def calculate(n, **kwargs):
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)


calculate(2, add=3, multiply=5)


# ** kwargs
class Car:

    def __init__(self, **kwargs):
        # using kwargs.get(model) instead of kwargs[model] allows empty values to not error
        self.make = kwargs.get("make")
        self.model = kwargs.get("model")


my_car = Car(make="nissan")
print(my_car.make)
print(my_car.model)
