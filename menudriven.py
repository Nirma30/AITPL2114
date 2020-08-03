num1 = int(input("enter the first value: "))
num2 = int(input("enter the second value: "))


def operation():

    print("OPERATIONS")
    print("1.addition")
    print("2.subtraction")
    print("3.multiplication")
    print("4.division")
    print("5.exit")
    x = int(input("enter your choice: "))
    if x == 1:
        num3 = num1 + num2
        print("the sum is: ", num3)
    elif x == 2:
        num3 = num1 - num2
        print("the difference is: ", num3)
    elif x == 3:
        num3 = num1 * num2
        print("the product is: ", num3)
    elif x == 4:
        num3 = num1 / num2
        print("the division is: ", num3)
    elif x == 5:
        exit()
    else:
        print("invalid input!!try again")


operation()
