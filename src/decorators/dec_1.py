# The golden rule of decorators: always return wrapper — never execute the logic directly inside the decorator.


def print_something(func):
    def wrapper():          # wrap the behavior
        print("hi chandu")
        func()
        print("hi nikitha")
    return wrapper          # return the wrapper, don't execute yet


@print_something
def say_hello():
    print("hi nikitha-chandu")


say_hello()  # now this calls wrapper(), not None()
