# Dictionary
# Collection of key value pairs
# Unordered
# All keys must be distinct
# Values may be repeated
# uses hashing internally, similar to sets

d = {110: "xyz", 101: "abc", 105: "bcd", 104: "abc"}

print(d)

d = {}
d["laptop"] = 1000
d["mobile"] = 2000
d["earphone"] = 3000
print(d)
print(d["mobile"])
print(d.get("hi", "NA"))

d = {110: "abc", 101: "xyz", 105: "pqr", 106: "bcd"}
d[101] = "wxy"
print(len(d))
print(d)
print(d.pop(105))
print(d)
del d[106]
print(d)
d[108] = "cde"
print(d.popitem(1)) # Removes last element added as a tuple 