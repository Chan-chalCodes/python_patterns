row = int(input("Enter number of rows:"))
for i in range(1, row+1):
    print("*", end="")
    for j in range(row-2):
        print("_", end="")
    print("*", end="")
    print()