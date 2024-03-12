# Python uses unicode and not ascii

print(ord("a"))  # prints ascii value
print(ord("A"))
print(chr(97))  # prints respective character for ascii value
print(chr(65))

s = 'hello'
print(s)
print(s[0])
print(s[-1])
print(s[1])
print(s[-2])

#  s[0] = e  strings are immutable

s = """Hi
This is Jayanth
Vegesna """

print(s)

# Escape Sequences

s = 'Hi\n Welcome to Jayanth\'s program'
s1 = "A simple \ example"
s2 = "Backlash at the end \\"
s3 = "\\n"  # to print backlash on screen
s4 = "\\f"
print(s, s1, s2, s3, s4)

s5 = r"C:\project\name.py"  # creating a raw string
print(s5)
