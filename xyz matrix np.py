import numpy as np
x = np.array([[1, 2], [3, 4], [5, 6], [7, 8]])
print(x)
y = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print(y)
z = np.array([[1, 2], [3, 4]])
print(z)
a = x.dot(z)
print(a)
b = a.dot(y)
print(b)
print("...............")
c = z.dot(y)
print(c)
print("...............")
# print(b+a+x)
