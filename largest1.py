l1 = []
n = int(input("enter the number of elements: "))
for i in range(0, n):
    ele = input()
    l1.append(ele)

l1.sort()
print(l1)
print("the largest number is: ", l1[-1])
