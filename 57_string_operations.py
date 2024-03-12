s1 = "Jayanth"
s2 = "Jay"

# Checking for substring
print(s2 in s1)
print(s2 not in s1)

# Concatenation
s1 = "Hello"
s2 = "hi"
s3 = s1 + s2
print(s3)

# Other string operations
s1 = "Jay"
s2 = s1.upper()
print(s2)
print(s2.isupper())  # Same is applicable for lowercase


s = "Hello my name is Jay"
print(s.startswith("Hello"))
print(s.endswith("Jay"))
print(s.startswith("Hello", 1))  # takes an additional parameter for start


s = s.split(",")  # can provide a seperator (example (,))
print(s)
print(' '.join(s))

s = "---Jay---"
print(s.strip("-"))
print(s.lstrip("-"))

s1 = "Hello this is Jay"
s2 = "Jay"
print(s1.find(s2))  # different from index function as when string not present then -1 returned
