a = int(input("Choose a number for a: "))
b = int(input("Choose a number for b: "))
c = int(input("Choose a number for c: "))

a, b, c = b, c, a

print("The numbers have been swapped")

print(f"Here is the result: a = {a}, b = {b}, c = {c}" )