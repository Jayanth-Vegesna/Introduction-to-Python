l = [10,20,30,40,50, "Jay"]

print(l)
print(l[0],l[3])
print(l[-1], l[-2])
l.append("Vegesna")     # adds object to end of list
l.insert(1,15)  # adds object to specific index moving other objects
print(l)
print(15 in l) # checks if object is present in list
print(l.count(30)) # checks count in list
print(l.index(30)) # checks first occurance of list
print(l.index("Jay",4,7))  # search index from start(inclusive) and end(exclusive)
l.remove(20)
print(l)
l.pop(5) # remove item based on index, if no argument then remvoes last item
print(l)
del l[5]
print(l)
del l[0:3] # removes items starting from 0 (inclusive) and uptill 3(exclusive) deosnt include 3
print(l)
print(min(l))
print(max(l))
print(sum(l))
l.reverse()
print(l)
l.sort()
print(l)