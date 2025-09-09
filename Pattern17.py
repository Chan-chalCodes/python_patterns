n = int(input("Enter number of rows: "))
for i in range(1, n+1):
    if i == (n//2 + 1):
        print("*")
    else:
        print("* *")