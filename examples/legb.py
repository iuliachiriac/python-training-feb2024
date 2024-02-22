X = "X"


def func(a):
    b = 1
    # global X  # access modifier used to change global variables
    # X = "AAA"

    def inner(c):
        d = 11

        # nonlocal b  # access modifier used to change outer scope variables
        # b = 11111

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


if __name__ == "__main__":
    # sum = 0  # shadowing
    func(2)

    print("Built-in names:", sum, print, int)
    print("Global names:", X, func, MyClass)
