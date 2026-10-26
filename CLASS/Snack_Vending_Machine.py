def calculate_change(paid, price):
    change = paid - price
    return change

snack_price = 25
print("========SNACK VENDING MACHINE========")
print(f"This snack costs {snack_price}")
print("COINS ACCEPTED: 1, 5, 10, 25\n")

total_inserted = 0
coins_inserted = 0

while True:
    coin = int(input("Insert a coin: "))
    if coin != 1 and coin != 5 and coin != 10 and coin != 25:
        print("\n=====INVALID COIN=====")
        print("try again\n")
        continue
    total_inserted += coin
    coins_inserted += 1
    print(f"Inserted: {coin}\nTotal so far: {total_inserted}")
    if total_inserted >= snack_price:
        print("Enough money paid\n")
        break

change_due = calculate_change(total_inserted, snack_price)

print("Snack coming!")

if change_due == 0:
    pass
else:
    print(f"The change is {change_due}")

print("\n=======Purchase Summary=======")
print(f"Snack price: {snack_price}")
print(f"Coins inserted: {coins_inserted}")
print(f"Total paid: {total_inserted}")
print(f"Change due: {change_due}")
print("==============================")
print("Thanks for your perchase")