x = input("enter the string: ")


def sortedsent():
    words = x.split(" ")
    words.sort()
    y = " ".join(words)
    return y


print(sortedsent())
