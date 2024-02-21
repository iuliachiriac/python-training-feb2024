X = "X"


def func(a):
    b = 1

    def inner(c):
        d = 11

        print("Built-in names:", sum, print, int)
        print("Global names:", X, func, MyClass)
        print("Enclosing names:", a, b, inner)
        print("Local names:", c, d, end='\n\n')

    # sum = 0  # shadowing
    # X = 0  # shadowing

    inner(22)

    print("Built-in names:", sum, print, int)
    print("Global names:", X, func, MyClass)
    print("Local names:", a, b, inner, end='\n\n')


class MyClass:
    pass


# sum = 0  # shadowing
func(2)

print("Built-in names:", sum, print, int)
print("Global names:", X, func, MyClass)
