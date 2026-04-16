import sys


a = [] # we are referring to a list count =1


print(sys.getrefcount(a))


b = a
print(sys.getrefcount(b))


del b
print(sys.getrefcount(a))



