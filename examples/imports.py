import math
import sys

import functions
import func_params as params
from legb import MyClass, func as legb_func
import pypackage.pymodule
# from pypackage import pymodule

print(f"The name of imports.py module is {__name__}")

print(sys.path)

print(type(functions), functions.__name__, functions.__file__)
functions.greet("Jane")

print(type(math), math.__name__, math.__file__)
print(math.sqrt(100))

params.modify_str("test")

print(MyClass, legb_func)
