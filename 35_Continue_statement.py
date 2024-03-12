# continue statement

List = [10, 16, 17, 18, 19, 15]
for x in List:
    if x % 5 == 0:
        continue
    print(x)

i = 0
while i <= 5:
    if i == 3:
        i = i + 1
        continue
    print(i, i*i)
    i = i + 1