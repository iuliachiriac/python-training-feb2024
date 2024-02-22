class Person:
    count = 0  # class attribute

    def __init__(self, name):
        self.name = name  # instance attribute
        Person.count += 1

    def greet(self, greeting="hi"):  # instance method
        print(f"{greeting.capitalize()}! I am {self.name}.")


if __name__ == "__main__":
    p1 = Person("Anna")
    print(p1.name, p1.count)

    p2 = Person("Mike")
    print(p2.name, p2.count)

    print(Person.count, p1.count is Person.count, p2.count is Person.count)

    p1.greet()
    p2.greet("hello")
