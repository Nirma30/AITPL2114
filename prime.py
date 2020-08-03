num = int(input("enter the value: "))
for i in range(2, num):
    if num % i == 0:
        print("the given value is not a prime number")
        break
else:
    print("the given value is a prime number")
