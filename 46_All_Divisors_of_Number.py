a = int(input("Enter a: "))

for x in range(1, a+1):
    if a % x == 0:
        print(x)
    x = x+1