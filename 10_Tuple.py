# tuple type
# faster than list
# cannot be modified, tuple is immutable

t = (10,20, "hi")
print(t)
t = ()
print(type(t))
t = (10,) # single item tuple, without comma type is taken as int or string dependent on argument

t = (10,20,30,40,50,10)
print(t[2])
print(t[-1])
print(t[1:3])
print(len(t)) # length
print(t.count(10))
print(t.index(30))