import functools


def make_pretty(func):  # func = ordinary, greet, decrement
    @functools.wraps(func)
    def inner(*args, **kwargs):
        print("I got decorated")
        return func(*args, **kwargs)
    return inner


@make_pretty
def ordinary():
    print("I am ordinary")


@make_pretty
def greet(name, greeting='hello'):
    print(f"{greeting.capitalize()}, {name}!")


@make_pretty
def decrement(nr, step=1):
    """Decrements nr by step"""
    return nr - step


# Decorating the function means replacing it with the decorator's return function
# print("ordinary id before decoration", id(ordinary))
# print("make_pretty id before decoration", id(make_pretty))
# ordinary = make_pretty(ordinary)  # make_pretty.<locals>.inner
# print("ordinary id after decoration", id(ordinary))
# print("make_pretty id after decoration", id(make_pretty))

ordinary()  # make_pretty.<locals>.inner()

greet("Anna")  # make_pretty.<locals>.inner("Anna")
greet("Anna", greeting="hi")

result = decrement(10, 2)  # make_pretty.<locals>.inner(10, 2)
print("decrement result:", result)

print(decrement.__name__, decrement.__doc__)
