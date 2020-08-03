l1 = []
n = int(input("enter the number of elements: "))
for i in range(0, n):
    ele = input()
    l1.append(ele)

l1.sort()
print(l1)
print("the third smallest number is: ", l1[2])
print("the fifth smallest number is: ", l1[4])
