acuatal_cost = int(input("What is the cost of making: "))
sales_price = int(input("What is the sale price: "))

if sales_price > acuatal_cost:
    print("You are making", sales_price - acuatal_cost, "in profit")
else:
    print("You are losing", acuatal_cost - sales_price, "in loss")