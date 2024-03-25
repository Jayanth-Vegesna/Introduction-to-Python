# end and sep in print()
print("Hello", end="  ")
print("Welcome")
print("14", "01", "2024", sep="-")

# % is overloaded by the string class to perform string formatting. Therefore, it is often called a string modulo
# (or sometimes even called modulus) operator.

# print integer and float value
print("Geeks : %2d, Portal : %5.2f" % (1, 05.333))  # tuple with value, format string, and String modulo operator

# print integer value
print("Total students : %3d, Boys : %2d" % (240, 120)) # %[flags][width][.precision]type

# print octal value
print("%7.3o" % 25)

# print exponential value
print("%10.3E" % 356.08977)

cstr = "I love geeksforgeeks"

# Printing the center aligned
# string with fill chr
print("Center aligned string with fillchr: ")
print(cstr.center(40, '#'))

# Printing the left aligned
# string with "-" padding
print("The left aligned string is : ")
print(cstr.ljust(40, '-'))

# Printing the right aligned string
# with "-" padding
print("The right aligned string is : ")
print(cstr.rjust(40, '-'))