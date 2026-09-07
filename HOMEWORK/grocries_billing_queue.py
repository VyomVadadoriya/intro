vegetables = 2.50
milk = 5.00
cheese = 7.50
fruits = 2.50
cookies = 6.00
snacks = 9.00
chips = 3.50

print("==================")
print("ITEMS:")
print("==================")
print("vegetables")
print("==================")
print("fruits")
print("==================")
print("chips")
print("==================")
print("milk")
print("==================")
print("cookies")
print("==================")
print("cheese")
print("==================")
print("snacks")
print("==================")

budget = int(input("What is your budget: "))

while budget > 0:
    purchase = input("First item: ")
    budget = budget - purchase
    items_sold += 1
    money_made += purchase
    if budget < 0:
        print("Too expensive")
    elif purchase is "end":
        print("The amount of items old is", items_sold)
        print("The amount of money_made is $", money_made)
    else:
        print("Invalid item")
    continue

print("THANK YOU")