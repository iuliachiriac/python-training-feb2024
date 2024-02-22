def compute(a, b, operation):
    return operation(a, b)


def get_sum(a, b):
    return a + b


print(compute(10, 3, get_sum))  # get_sum(10, 3)
print(compute(10, 3, pow))
print(compute(10, 3, lambda x, y: x - y))
print(compute(10, 3, lambda x, y: x * y))


l = [1, 1, 2, 3, 3, 4, 4, 5, 6, 7, 9]
for elem in filter(lambda x: x % 2 == 0, l):
    print(elem)
