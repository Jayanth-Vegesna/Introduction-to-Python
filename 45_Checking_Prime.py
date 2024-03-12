a = int(input("Enter a: "))
if a <= 1:
    print("No")
else:
    for i in range(2,a):
        if a % i == 0:
            print("No")
            break
    else:   # Else condition is executed when for loop breaks otherwise if is excuted
        print("Yes")
