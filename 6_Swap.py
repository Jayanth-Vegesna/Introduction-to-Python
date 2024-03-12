#Swaping two variables

# extra variable
x=100
y=20
print("X = ", x,"Y = ", y)
temp = x
x = y
y = temp
print("X = ", x,"Y = ", y)

# Comma Assignment
a = 30
b = 20
print("A = ", a,"B = ", b)
a,b = b,a
print("A = ", a,"B = ", b)

x,y,z = 100, 200, "Jay"
print(x,y,z)
x,y,z = x+100, y-500, z+" Vegesna"
print(x,y,z)

