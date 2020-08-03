l1 = []
n = int(input("enter the number of elements: "))
for i in range(0, n):
    ele = input()
    l1.append(ele)

l1.sort()
print(l1)
print("the second largest number is: ", l1[-2])
print("the fourth largest number is: ", l1[-4])