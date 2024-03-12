# Basic format for function
# Useful to repeat a certain portion of code multiple times

# Applications of functions:
# 1. Avoid code redundancy and easy maintenance
# 2. Make code modular
# 3. Abstraction
# 4. Avoid variable name collisions

# lambda is used to declare concise functions
def fun():
    print("fun() called")


def printDate(d, m, y):
    print(d, m, y, sep='-')


def getData(d, m, y):
    return d + "-" + m + "-" + y


print("Before Calling fun()")
fun()
print("After Calling function")
print("India has become independent on ")
printDate("15", "08", "1947")
x = getData("15", "08", "1947")
print(x)
