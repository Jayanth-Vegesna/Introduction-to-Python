n = int(input("Enter number: "))
res = 1
for i in range(2, n+1):
    res = res* i
print(res)

# Using math function
import math
n = int(input("Enter n:"))
res = math.factorial(n)
print("Factorial is: ", res)
