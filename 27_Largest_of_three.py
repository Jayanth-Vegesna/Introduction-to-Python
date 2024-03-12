a = int(input("Enter a"))
b = int(input("Enter b"))
c = int(input("Enter c"))

# More comparisons
if (a >= b) and (a >= c):
    print(a)
elif (b >= c) and (b >= a):
    print(b)
elif (c >= a) and (c >= b):
    print(c)
else:
    print("Not a number")

# Less Comparisons
if a >= b:
    if a >= c:
        print(a)
    else:
        print(c)
elif b >= c:
    print(b)
else:
    print(c)

# max function
print(max(a, b, c))
