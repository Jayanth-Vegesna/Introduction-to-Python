# nested loops
x = int(input("Enter number of tables to print: "))
for i in range(1, x+1):
    for j in range(i, i*10+1, i):
        print(j, end=' ')
    print()

# to print list of list
ll = [[10,20, 30], [40, 50, 60], [70, 80]]
for i in ll:
    for x in i:
        print(x, end=' ')
    print()