# Break statement

# Check for the LCM
n = int(input("Enter n: "))
for x in range(3, n+1):
    if n % x == 0:
        print(x)
        break

x = 2
while x <= n:
    if n % x == 0:
        print(x)
        break
    x = x+1
