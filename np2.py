import numpy as np
x = np.array([1, 2, 3, 4, 5], ndmin=3)
print(x)
y = np.arange(24)
print(y)
z = y.reshape(2,4,3)
print(z)
a = y.reshape(1,8,3)
print(a)
