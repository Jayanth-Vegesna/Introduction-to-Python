# and operator
# not operator
# or operator

a = 10
b = 20
c = 30

# returns true or false based on the logical operation
print(a < b and b < c)
print(a < b or b > c)
print(not a > b) # unary operator

# short-circuiting in the case that the first condition is false for AND operator then 2nd condition is not evaluated
# same case in OR operator if first condition is true then 2nd condition is not considered

# AND and OR operator can operate on non-boolean type
# Works on containers, list, string etc.

s1 = ""
s2 = s1 or "DefaultStr"
print(s2)

x = 10
print(x or 20)  # Non-zero integer is treated as true, returns last evaluated value taking into account short-circuiting
y = 0
print(y or 30)
z = 40
print(z and 50)

