
import math


def getFirstDigit(x):
    d = int(math.log10(x))
    res = x//(10**d)
    return res


def First(number):
    while number >= 10:
        number = number//10  # Floor division operator
    return number


num = int(input("enter number"))
print(First(num))

x = int(input("Enter X:"))
print(getFirstDigit(x))