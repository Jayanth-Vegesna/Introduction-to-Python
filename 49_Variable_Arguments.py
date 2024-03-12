def summ(*elements):  # becomes a tuple, positional variable length arguments
    res = 0
    for x in elements:
        res = res + x
    return res


def printDetails(**details):  # Keyword variable length arguments, uses a dictonary
    for d, v in details.items():
        print(f"{d} is {v}")


printDetails(id=101, name='abc', price=100)
print()
printDetails(id=102, name="xyz")

print(summ(10, 20))
print(summ(10, 20, 30))
print(summ(10))
print(summ())

