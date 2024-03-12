# Multiplication table of user inputted number

number = int(input("Enter a number: "))
multiples = int(input("Enter another number: "))

for i in range(1, multiples+1):
    print(number*i)

i = 1

while i <= multiples:
    print(number*i)
    i += 1
