row = int(input("Enter number of rows:"))
for i in range(1, row+1):
    for j in range(row-i):
        print("_", end=" ")
    for j in range(i):
        print("*", end=" ")
    print()