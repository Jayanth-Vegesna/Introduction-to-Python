# is and is not operator

x = 10
y = x
print(x is y)  # Returns true if two values have same ID(stored in same memory location)
print(x is not y)  # IS NOT returns opposite of IS

# python does not allocate new location for same literals, just refers to same ID
x1 = 10
x2 = 10
y1 = 10.5
y2 = 10.5
z1 = "Hi"
z2 = "Hi"
print(x1 is x2)
print(y1 is y2)
print(z1 is z2)

# IS only true in the case of literals not containers
l1 = [10, 20, 30]
l2 = [10, 20, 30]
print(l1 is l2)