
def validate_positive(func):
    def wrapper(*args, **kwargs):
        for arg in args:
            if arg < 0:
                raise ValueError("Argument must be positive")
        result = func(*args, **kwargs)
        return result
    return wrapper

@validate_positive
def multiply(a, b):
    return a * b

print(multiply(3, 4))   # should work fine
print(multiply(-1, 4))