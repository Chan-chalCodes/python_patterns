row = int(input("Enter number of rows:"))
for i in range(1, row+1):
    for j in range(row-i+1):
        print("*", end="")
    for j in range(2*i-2):
        print(" ", end="")
    for j in range(row-i+1):
        print("*", end="")
    print()
