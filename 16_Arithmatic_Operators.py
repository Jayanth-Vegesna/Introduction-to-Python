# Arithmatic operators
# +	Addition: adds two operands	x + y
# –	Subtraction: subtracts two operands	x – y
# *	Multiplication: multiplies two operands	x * y
# /	Division (float): divides the first operand by the second	x / y
# //	Division (floor): divides the first operand by the second	x // y
# %	Modulus: returns the remainder when first operand is divided by the second	x % y
# **	Power : Returns first raised to power second	x ** y

x = 4
y = 9
print(x + y)
print(x - y)
print(x * y)
print(x / y)
print(x // y)  # Quotient(divisible)
print(x % y)  # Remainder operator/ Modular division
print(x ** y)  # raise power operator


x = -5
y = 2
print(x//y)
x = 5.0
y = 2
print(x//y)
x = 2
y = -2
print(x**y)

# Precedence of operators
print(5 + 2*3)

# Associativity of operators (mostly left to right)  (power of operator right to left) 
print(2**2**-1)
print((2**2)**-1)
