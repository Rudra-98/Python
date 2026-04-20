def print_name(func):
    def wrapper(*args, **kwargs):
        print(func(*args, **kwargs))
    return wrapper


@print_name
def greet(name):
    return f"Hello, {name}!"

greet("Chandu")