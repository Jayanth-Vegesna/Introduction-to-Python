# triangle pattern

x = int(input())

for i in range(x):
    for j in range(i+1):
        print("*", end=' ')
    print()

for i in range(x):
    for j in range(x-1-i):
        print("*", end=' ')
    print()
    