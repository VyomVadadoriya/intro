try:
    n = int(input("Enter a number: "))
    print(f"You chose {n}.")
except ValueError as ex:
    print("Exception:", ex)

print("\nTEST")