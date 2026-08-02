import time
#
def task(name):
    print(f"Start {name}")
    time.sleep(2)
    print(f"End {name}")

task("A")
task("B")
#
#
#
# # shallow copy and deep copy
# #assume a = [[3,4],[1,2]]
# # In shallow copy , This is the key concept of shallow copy:
#
# # b.append(5)                                               ❌ No — outer list is a new object
# # b[0].append(9)                                            ✅ Yes — inner objects are shared
#
# #
# #
# # One liner to remember:
# #
# # Shallow copy → new outer object, but shared inner objects
# # Deep copy → new outer object, and brand new inner objects too


import copy

a = [[1,2],[3,4]]
b = copy.copy(a)


print(a)

print(b)

b[0].append(6)

print(b)
print(a)


c  = copy.deepcopy(b)

c[1].append(10)


print(c)

print(b)




