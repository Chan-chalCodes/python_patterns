row = int(input("Enter number of rows:"))
for i in range(row, 0, -1):
    print("*", end="")
    for j in range(i):
        print("_", end="")
    print("*", end="")
    print()
