x = list(map(input("enter the elements: "), x))
for i in x:
    x.sort()
print("the second largest number is:", x[1])
print("the fourth largest number is: ", x[3])
