print("========================")
print("== ATM CASH DISPENSER ==")
print("========================")
total_100 = total_50 = total_20 = total_10 = total_10 = total_5 = total_2 = total_1 = 0
customers_servered = 0
total_dispensed = 0

serving = True
while serving:
    name = input(" == Enter Name:  == ")
    amount = int(input(f"Hello {name}! Enter amount of money to withdraw: "))
    if amount <= 0:
        print(" === INVALID AMOUNT === \n == ENTER A POSITIVE NUMBER ==")
        continue

    print(f"\nDispensing ${amount} for {name}")
    remaining = amount
    idx = 1
    while idx <= 7:
        if idx == 1: value = 100
        elif idx == 2: value = 50
        elif idx == 3: value = 20
        elif idx == 4: value = 10
        elif idx == 5: value = 5
        elif idx == 6: value = 2
        else: value = 1
        count = remaining // value
        if count > 0:
            print(f" ==== {count} ${value} bills ==== ")
            remaining -= count * value
            if value == 100: total_100 += count
            elif value == 50: total_50 += count
            elif value == 20: total_20 += count
            elif value == 10: total_10 += count
            elif value == 5: total_5 += count
            elif value == 2: total_2 += count
            else: total_1 += count
        idx += 1

    customers_servered += 1
    total_dispensed += amount
    print(f"Transaction complete")
    again = input("New customer? Y/n: ")
    if again != "Y":
        serving = False

print("\n === DAILY DENOMINATION REPORT === ")
for slot in range(1, 8):
    if slot == 1: value, total = 100, total_100
    elif slot == 2: value, total = 50, total_50
    elif slot == 3: value, total = 20, total_20
    elif slot == 4: value, total = 10, total_10
    elif slot == 5: value, total = 5, total_5
    elif slot == 6: value, total = 2, total_2
    else: value, total = 1, total_1
    if total > 0:
        print(f"${value} bills dispensed : {total} ", end="")
        for note in range(total):
            print("=", end="")
        print()

print(f"\nCustomers served : {customers_servered}")
print(f"Total dispensed : {total_dispensed} bills")
print(" == ATM session closed == ")