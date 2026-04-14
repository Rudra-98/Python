#Variable positional arguments
#Lets a function accept any number of positional arguments as a tuple.

#Variable keyword arguments
#Lets a function accept any number of named arguments as a dictionary.
#
# Real-world use case — when building wrapper functions or decorators where you don't know what arguments the original function takes:
#
# Order matters: *args must always come before **kwargs

def describe(*args, **kwargs):
    print("Positional:", args)
    print("Keyword:", kwargs)

describe(1, 2, 3, name="Alice", city="Bangalore")
# Positional: (1, 2, 3)
# Keyword: {'name': 'Alice', 'city': 'Bangalore'}