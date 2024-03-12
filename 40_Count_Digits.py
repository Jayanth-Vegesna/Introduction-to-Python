x = int(input("Enter a number: "))
res = 0
while x > 0:
    x = x//10
    res = res + 1
print(" Digit Count is: ", res)
