class Error(Exception):
    pass

class dobException(Error):
    pass



age = int(input("Enter your age: "))

try:
    if age<=30 and age>=18:
        print("You are old enough")
    else:
        raise dobException
except dobException:
    print("You are not old enough to apply")