import sys
print("Enter an operation\n 1. Add\n 2. Subtract\n 3. Multiply\n")  # Can be done using triple quoted strings
x = int(input("Select an operation from 1 to 3: "))
if x not in (1, 2, 3):
    print("invalid choice")
    sys.exit()
a = int(input("Enter number 1: "))
b = int(input("Enter number 2: "))
if x == 1:
    print("Addition of two numbers is: ", a+b)
elif x == 2:
    print("Subtraction of two numbers is: ", a-b)
elif x == 3:
    print("Multiplication of two numbers is: ", a*b)

# Ternary operator can be used to perform the same operation
# {(condition1 :  <code1>) , (condition2 :  <code2>) }.get(True, <code3>)
