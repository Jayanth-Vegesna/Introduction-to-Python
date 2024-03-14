# Syntax: type(object, bases, dict)

# Parameters :
# object: Required. If only one parameter is specified, the type() function returns the type of this object
# bases : tuple of classes from which the current class derives. Later corresponds to the __bases__ attribute.
# dict : a dictionary that holds the namespaces for the class. Later corresponds to the __dict__ attribute.

# Return: returns a new type class or essentially a metaclass.


# Checking Object type
a = ("Geeks", "for", "Geeks")
b = ["Geeks", "for", "Geeks"]
c = {"Geeks": 1, "for": 2, "Geeks ": 3}
d = "Hello World"
e = 10.23
f = 11.22

print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))
print(type(f), '\n')

# Checking Object Parameter

print(type([]) is list)

print(type([]) is not list)

print(type(()) is tuple)

print(type({}) is dict)

print(type({}) is not list)