# Find last digit of a user inputted number
x = int(input("Enter X"))
ld = abs(x) % 10  # Without abs function the program doesnt work for negative numbers
print("Last digit is", ld)
