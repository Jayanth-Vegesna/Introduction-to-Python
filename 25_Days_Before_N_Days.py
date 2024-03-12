# Days before N days assuming 0 is sunday and saturday is 6
x = int(input("Enter a number from 0 to 6: "))
y = int(input("Enter number of days: "))
print((x - y) % 7)