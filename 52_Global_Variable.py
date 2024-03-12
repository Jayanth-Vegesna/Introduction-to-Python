
def fun():
    x = 10
    globals()['x'] = 20
    print(x)


x = 15
fun()
print(x)

