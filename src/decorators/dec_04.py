from functools import wraps

# Without wraps
def bad_decorator(func):
    def wrapper(*args, **kwargs):
        """Wrapper function"""
        return func(*args, **kwargs)
    return wrapper

@bad_decorator
def add(a, b):
    """Adds two numbers"""
    return a + b

print(add.__name__)      # Output: wrapper (WRONG!)
print(add.__doc__)       # Output: Wrapper function (WRONG!)

# With wraps
def good_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        """Wrapper function"""
        return func(*args, **kwargs)
    return wrapper

@good_decorator
def multiply(a, b):
    """Multiplies two numbers"""
    return a * b

print(multiply.__name__)  # Output: multiply (CORRECT!)
print(multiply.__doc__)   # Output: Multiplies two numbers (CORRECT!)