# Pass by value
def fun(x):
    print(id(x))
    x = 15  # Local Variable
    print(id(x))


def funl(l):
    print(id(l))
    l.append(15)
    print(id(l))


x = 10  # Global Variable
fun(x)
print(id(x))
print(x)

l = [10, 20, 30]
funl(l)
print(l)
print(id(l))
