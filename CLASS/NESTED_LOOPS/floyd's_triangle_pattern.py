print("Floyd's pyramid pattern")
n = int(input("Enter the number of rows: "))

number = 0

for i in range(n):
    for j in range(i + 1):
        number += 1
        print(number, end=" ")
    print()