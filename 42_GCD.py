a = int(input("Enter a: "))
b = int(input("Enter b: "))
small = min(a,b)
GCD = 1
for i in range(1, small+1):
    if a % i == 0 and b % i == 0:
        GCD = i
print(GCD)

# math library
import math
a = int(input("Enter a: "))
b = int(input("Enter b: "))
print(math.gcd(a,b))