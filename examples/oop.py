from datetime import date
import random


class Person:
    count = 0  # class attribute
    MIN_DATE_OF_BIRTH = date(1900, 1, 1)

    def __init__(self, name, date_of_birth):
        self.name = name  # instance attribute
        self.date_of_birth = date_of_birth
        self._increment_count()

    @property
    def date_of_birth(self):
        return self._date_of_birth

    @date_of_birth.setter
    def date_of_birth(self, value):
        if value < self.MIN_DATE_OF_BIRTH:
            raise ValueError("Invalid date of birth.")
        self._date_of_birth = value

    @property
    def age(self):
        return self.compute_age(self._date_of_birth)

    def greet(self, greeting="hi"):  # instance method
        print(f"{greeting.capitalize()}! I am {self.name}.")

    @classmethod
    def _increment_count(cls):  # class method
        cls.count += 1

    @staticmethod
    def compute_age(date_of_birth):
        diff = date.today() - date_of_birth
        years = int(diff.days / 365.25)
        return years

    def __str__(self):
        return f"{self.__class__.__name__} object (name={self.name})"

    def __repr__(self):
        return self.__str__()

    def __lt__(self, other):
        return self.date_of_birth > other.date_of_birth


class Student(Person):
    count = 0

    def __init__(self, name, date_of_birth, university):
        super().__init__(name, date_of_birth)
        self.university = university

    def greet(self, greeting="hello"):
        print(f"{greeting.capitalize()}! I am {self.name} and I study at "
              f"{self.university}.")

    def get_grade(self, subject):
        return random.randint(2, 10)  # fetch grade from db

    def __str__(self):
        super_str = super().__str__()
        return f"{super_str} (univ={self.university})"


if __name__ == "__main__":
    p1 = Person("Anna", date(2000, 5, 1))

    print(p1.name, p1.count)  # get attribute
    p1.name = "Ana"  # set attribute

    p2 = Person("Mike", date(1984, 6, 23))
    print(p2.name, p2.count)

    print(Person.count, p1.count is Person.count, p2.count is Person.count)

    p1.greet()
    p2.greet("hello")

    print(p1, p2, repr(p1))

    p3 = Person("Jane", date(1994, 11, 3))
    persons = [p1, p2, p3]
    persons.sort(reverse=True)
    print("Persons sorted old -> young:", persons)

    # print(Person.compute_age(date(1800, 4, 3)))

    try:
        p1.date_of_birth = date(1800, 5, 2)  # set attribute
    except ValueError as ex:
        print(f"Date of birth not changed: {ex} {p1.name}'s age: {p1.age}")

    s1 = Student("Ion Popescu", date(2001, 7, 22), "Politehnica București")
    s1.greet()
    print(f"{s1.name} is {s1.age} years old and is a student at "
          f"{s1.university} and got a {s1.get_grade('math')} in Math.")

    print(s1)
    print(Student.mro())  # method resolution order

    print("Person count:", Person.count, "\nStudent count:", Student.count)
