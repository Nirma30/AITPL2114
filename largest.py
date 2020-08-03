a = input("enter the first value: ")
b = input("enter the second value: ")
c = input("enter the third value: ")
if a > b and a > c:
    print(a, " is the largest value")
elif b > a and b > c:
    print(b, "is the largest value")
else:
    print(c, "is the largest value")
