# in operator and not in operator

s = "Hello"
print("l" in s) # Checks for substring
print("lo" in s)
print("lke" in s)

d = {10: "abc", 20: "efg"}
print(10 in d)  # Checks for key not value
print("abc" in d)

l = [10, 20, 30, 40, 50]
print(90 not in l)  # Checks for membership (List, Set, Tuple, Dict, etc.)
print(20 in l)
print([10,30] in l)
