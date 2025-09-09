n = int(input("Enter number of rows: "))
for i in range(1, n+1):
    print("*", end=" ")
print()

for i in range(0, n-2):
    for j in range(0, 2):
        print("*", end=" ")
    print()

for i in range(1, n+1):
    print("*", end=" ")
print()