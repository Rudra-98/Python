# Generator are the simplest way to create iterators.

# Regular function — computes ALL values at once, stores in memory
def square_list(x):
    return [i**2 for i in range(x)]  # entire list in memory

# Generator — computes ONE value at a time, lazy evaluation
def square(x):
    for i in range(x):
        yield i**2  # pauses here, resumes on next()

square_gen = square(5)

print(next(square_gen))
print(next(square_gen))
print(next(square_gen))
