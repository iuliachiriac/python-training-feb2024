"""This is a docstring exemplifying docstring creation for a module"""

x = -10  # numeric literal
print("hello world")

text = "hello"  # string literal
print(text)

command = \
    "/Users/iulia/PycharmProjects/python-training-feb2024/.venv/bin/python "\
    "/Users/iulia/PycharmProjects/python-training-feb2024/examples/script.py "
print(command)

my_shopping_list = ['apples', 'bananas', 'oranges', 'pears', 'peaches',
                    'cherries']

# Comments start with # symbol and explain the code
if x > 0:
    print("x is positive")
    print("inside if")
else:
    print("x is negative")

print("outside if")

multiline_str = """
import math
math.pi
math.sqrt(9)
"""
print(multiline_str)

sentence = "That\'s my \"job\". This is a backslash: \\"
print(sentence)
print("This" in sentence)

# F-strings
name = "   Ion Popescu\n \n\n"
age = 30

message = f"{name.strip()} is {age + 3} years old."
print(message)

first_name = 'Mike'
last_name = 'Clarkson'
accounts = 2
balance = 128.5532
print(f'{first_name:.1}. {last_name} has {accounts} bank accounts with a total '
      f'balance of {balance:.2f}$.')
