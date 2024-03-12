# if and elif condition

x = int(input("Enter a number"))

if x % 2 == 0:
    print("Even")
elif x % 2 == 1:
    print("Odd")
else:
    print("NaN")

if x > 0:
    print("positive")
elif x<0:
    print("negative")
else:
    print("zero")

x = int(input("Enter n1"))
y = int(input("Enter n2"))
if x > y:
    print("n1 is greater than n2")
elif x < y:
    print("n2 is greater than n1")
else:
    print("n1 and n2 are equal")

# Ternary operator can be used to perform the same operation
# {(condition1 :  <code1>) , (condition2 :  <code2>) }.get(True, <code3>)
