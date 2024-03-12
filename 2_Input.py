# input (): This function first takes the input from the user and converts it into a string.
# The type of the returned object always will be <type ‘str’>.
# It does not evaluate the expression it just returns the complete statement as String.
# For example, Python provides a built-in function called input which takes the input from the user.
# When the input function is called it stops the program and waits for the user’s input.
# When the user presses enter, the program resumes and returns what the user typed.

# Basic input
inp = input('Enter a Statement\n')
print(inp)

# Checking input type
num = input("Enter a number: \n")
name1 = input("Enter your name: \n")
print("type of number", type(num))
print("type of name", type(name1), "\n")

#taking integer input
num1 = int(input("Enter integer "))
print (num1, type(num1))
