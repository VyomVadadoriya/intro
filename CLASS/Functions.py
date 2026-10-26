def greet_customer():
    print("Welcome to the Lemonade Stand")
    print("Fresh lemonade made just for you")

greet_customer()

price_per_cup = float(input("What is the price of a cup: "))
cups_sold = int(input("Number of cups sold: "))

def calculate_total(price, cups):
    total = price * cups
    return total

total_cost = calculate_total(price_per_cup, cups_sold)

rounded_total = round(total_cost, 2)
print("total cost: ", rounded_total)

amount_paid = float(input("Amount paid by customer: "))

def calculate_change(paid, total):
    change = paid - total
    return change

change_due = calculate_change(amount_paid, rounded_total)
rounded_change = round(change_due, 2)

def thank_you_message(cups):
    if cups > 5:
        print("Big order, Thank you")
    else:
        print("Thanks for stopping by")

closing_message = thank_you_message(cups_sold)

print("Thanks for visiting the lemonade stand")