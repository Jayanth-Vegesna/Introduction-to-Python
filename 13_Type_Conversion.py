# Explicit type conversions

s = "jayanth"

print(list(s))
print(tuple(s))
print(set(s))

l = ['a', 'b', 'c']
print(str(l))  # String representation of list
a = 10
b = 11
print(str(a) + str(b))
c = 12.5
print(str(c))

t = (10, 20, 30)
print(list(t))
s = {10, 20, 30}
print(list(s))


a = 20
print(bin(a))   # Binary
print(hex(a))   # Hexadecimal
print(oct(a))   # Octal

a = "1001"
print(int(a,2))
b = "12"
print(int(b, 8))
c = "A1"
print(int(c, 16))
