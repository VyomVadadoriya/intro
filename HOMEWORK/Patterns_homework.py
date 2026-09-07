print("Half pyramid pattern with stars(*)")
n = int(input("Enter the number of rows: "))

for i in range(n):
    for j in range(i + 1):
        print("* ", end="")
    print()



print("Floyd's pyramid pattern")
n = int(input("Enter the number of rows: "))

number = 0

for i in range(n):
    for j in range(i + 1):
        number += 1
        print(number, end=" ")
    print()

print("Diamond pattern")
rows = int(input("Enter the number of rows: "))

for i in range(1, rows + 1):
    print(" " * (rows - i) + "*" * (2 * i - 1))

for i in range(rows - 1, 0, -1):
    print(" " * (rows - i) + "*" * (2 * i - 1))