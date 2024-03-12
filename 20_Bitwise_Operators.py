# Bitwise Operators
# Used for programming on a Hardware level (Device drivers)

print(bin(18))  # 0b is prefix for binary
# oct is for octal
print(int("01010110", 2))  # The base is 2nd operator
x = 3
y = 6
print(x & y)  # Bitwise And operator
print(x | y)  # Bitwise Or operator
print(x ^ y)  # Bitwise XOR operator

print(x << 2)  # Left shift operator
print(x >> 2)  # Right shift operator
print(~x)  # Not operator, The first bit representing sign is also toggled making it negative, and negative numbers
# are stored in 2's complement form

