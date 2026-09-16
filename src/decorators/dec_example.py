import functools
def validator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        for item in args:
            if item < 0:
                raise ValueError('The number cannot be negative')
        return func(*args, **kwargs)
    return wrapper



@validator
def multiple_validator(a,b):
    return a*b

print(multiple_validator(6,4))