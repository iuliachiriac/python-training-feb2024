def greet(name, greeting="hello", punctuation="!"):
    print(f"{greeting.capitalize()}, {name}{punctuation}")


greet("Ana")
my_name = "Ion"
greet(my_name, "hi")  # call function with positional arguments
greet(greeting="salut", name="George")  # keyword arguments
greet("George", punctuation=".")  # positional & keyword arguments

result = greet("Ana")
assert result is None


def decrement(nr, step=1):
    return nr - step


result = decrement(10)
assert result == 9
print(result)


def varargs(arg1, *args, kw1=None, **kwargs):
    print(arg1, kw1)
    print(args, type(args))
    print(kwargs, type(kwargs), end="\n\n")


# varargs()
varargs(1)
varargs(1, 2, 3)
# varargs(name="Ana", age=20)
varargs(4, 5, 6, 7, name="Ana", age=20)


name = '    Ion Popescu\n\n\n'
age = 36

person = {
    "name": name.strip(),
    "age": age,
}
person_tuple = (name.strip(), age)

print(f"1. My name is {name.strip()} and I am {age} years old")
print("2. My name is {} and I am {} years old".format(name.strip(), age))
print("3. My name is {0} and I am {1} years old".format(name.strip(), age))
print("4. My name is {name} and I am {age} years old".format(
    name=name.strip(), age=age))
# Argument unpacking
print("5. My name is {0} and I am {1} years old".format(*person_tuple))
print("6. My name is {name} and I am {age} years old".format(**person))
