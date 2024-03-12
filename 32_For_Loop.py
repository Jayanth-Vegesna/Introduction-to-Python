# For Loop
# for x in seq: 'seq' can be list, string, tuple, set, range...
#   statement 1

List = [10, 20, 30, 40]
for x in List:
    print(x)

for x in range(5):
    print(x)

for x in range(20):
    if x % 6 == 0:
        print(x)

List = [10, 20, 30, 40]  # gives item and index
for i in range(len(List)):
    print(i, List[i])
