print("Enter the following values of the Geometric Progression to find nth term")
print("The formula for the nth term in an Geomteric Progression is nth term = a*r^(n-1)")
a = int(input("Enter the first term: "))
r = int(input("Enter the common ratio(r): "))
n = int(input("Enter the nth term: "))
print("The value of nth term is: ", a*(r**(n*1)))