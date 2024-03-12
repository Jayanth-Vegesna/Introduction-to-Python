# Printing a square pattern using stars

x = int(input("Enter a number: "))

for i in range(x):
    for j in range(x):
        print("*", end =' ')
    print()