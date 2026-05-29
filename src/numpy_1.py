import numpy as np

np_array = np.array([1,2,3,4,5,6,7,8,9])

print(np_array)


print(np_array.shape)


print(np_array.size)


print(type(np_array))

print(np_array.dtype)


np_array_1 = np_array.reshape(1,9)
print(np_array_1)

a = np.array([[1,2,3,4],[5,6,7,8]])


print(a.size)

print(a.shape)

b = np.arange(0,10,1)


print(b)

print(b.reshape(1,10))


print(np.ones(10))


print(np.ones((3,4)))


print(np.eye(5))