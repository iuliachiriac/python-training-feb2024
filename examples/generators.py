def squares(start, stop):
    for nr in range(start, stop):
        yield nr ** 2


square_generator = squares(1000, 1010)
print("Values generated with next")
print(next(square_generator))
print(next(square_generator))

print("Values generated with for")
for sq in square_generator:
    print(sq)
