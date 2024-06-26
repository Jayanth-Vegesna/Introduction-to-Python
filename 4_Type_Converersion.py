# Implicit Type Conversion
# In Implicit type conversion of data types in Python, the Python interpreter automatically converts one data type to
# another without any user involvement.

# Explicit Type Conversion
# In Explicit Type Conversion in Python, the data type is manually changed by the user as per their requirement.
# With explicit type conversion, there is a risk of data loss since we are forcing an expression to be changed in some specific data type

# 1. int(a, base): This function converts any data type to an integer. ‘Base’ specifies the base in which the string is if the data type is a string.
# 2. float(): This function is used to convert any data type to a floating-point number.
# 3. ord(): This function is used to convert a character to integer.
# 4. hex(): This function is to convert integer to hexadecimal string.
# 5. oct(): This function is to convert integer to octal string.
# 6. tuple() : This function is used to convert to a tuple.
# 7. set() : This function returns the type after converting to set.
# 8. list() : This function is used to convert any data type to a list type.
# 9. dict() : This function is used to convert a tuple of order (key,value) into a dictionary.
# 10. str() : Used to convert integer into a string.
# 11. complex(real,imag) : This function converts real numbers to complex(real,imag) number.
# 12. chr(number): This function converts a number to its corresponding ASCII character.

#implict type conversion
x = 10
print("x is of type:", type(x))
y = 10.6
print("y is of type:", type(y))
z = x + y
print(z)
print("z is of type:", type(z))

# explict type conversion

s = "10010"

c = int(s, 2)
print("After converting to integer base 2 : ", end="")
print(c)

e = float(s)
print("After converting to float : ", end="")
print(e)