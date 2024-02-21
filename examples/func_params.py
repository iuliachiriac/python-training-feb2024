def modify_str(obj):
    print('id(obj) =', id(obj))
    obj += "x"  # a new string gets created
    print('id(obj) =', id(obj), '(after +=)')
    print('inside function:', obj)


print("----strings----")
my_str = "ceva"
print('id(my_str) =', id(my_str))
modify_str(my_str)
print('outside function:', my_str)


def modify_list(obj):
    print('id(obj) =', id(obj))
    obj += [5, 6]  # the list object is modified
    print('id(obj) =', id(obj), '(after +=)')
    print('inside function:', obj)


print("----lists----")
my_list = [1, 2, 3]
print('id(my_list) =', id(my_list))
modify_str(my_list)
print('outside function:', my_list)
