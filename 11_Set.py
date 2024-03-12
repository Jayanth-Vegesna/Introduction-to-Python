# Sets
# Distinct items, cannot have same items
# Unordered,no predefined order when printing can be random
# No indexing
# Mathematical set operations are fast (union, intersection, set difference etc. )
# User hashing internally

s1 = [20, 30, 40]
print(s1)

s2 = set([20, 30, 40])  # set constructor can add tuple
print(s2)

s3 = {}         # Dictionary
print(type(s3))

s4 = set()      # Empty set
print(type(s4))
print(s4)

# Adding elements
s = {10, 20}
s.add(30)
print(s)
s.add(30)   # no change
s.update([40, 50])
print(s)
s.update([90, 80], {60, 70})
print(s)

# Removing elements
s.discard(30)  # Does not do anything if element is not in the set
s.remove(20)  # provides an error if member doesn't exist, check membership before removing
print(s)
s.clear()
print(s)
s.add(30)
print(s)
del s   # Removes object


s = {10, 20, 30, 40}
print(len(s))
print(20 in s)

# Set theory operations
s1 = {2, 4, 6, 8}
s2 = {3, 6, 9}

print(s1 | s2)  # Union can be done with s1.union(s2)
print(s1 & s2)  # Intersection can be done with s1.intersection(s2)
print(s1 - s2)  # Subtraction can be done with s1.difference(s2)
print(s1 ^ s2)  # Symmetric difference, elements in either s1 or s2 but not both

s1 = {2, 4, 6, 8}
s2 = {4, 8}

print(s1.isdisjoint(s2))  # sets have no common elements
print(s1 <= s2)  # Subset s1 of s2 (false)
print(s1 < s2)  # Proper subset (doesnt allow equal sets)
print(s1 >= s2)  # Superset
print(s1 > s2) # Proper superset