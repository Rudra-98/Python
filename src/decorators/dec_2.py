#A decorator is a function that takes another function as input, adds some extra behavior, and returns a new function — without modifying the original function's code.


def validate_age(age):        # Level 1: accepts config (age)
    def decorator(func):      # Level 2: accepts the function
        def wrapper():        # Level 3: the actual replacement
            if age <= 18:
                print("You are not old enough to vote")
            else:
                print("You are old enough to vote")
                func()
        return wrapper
    return decorator          # Level 1 must return Level 2


@validate_age(19)
def say_hello():
    print("Hello World")


say_hello()
