# Generator are the simplest way to create iterators.


def square(x):
    for i in range(x):
        yield i**2

square_gen = square(5)

print(type(square_gen))
# for i in square_gen:
#     print(i)


print(next(square_gen))
print(next(square_gen))
print(next(square_gen))
