m = int(input("enter the starting range: "))
n = int(input("enter the ending range: "))
for num in range(m, n):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            print(num)
