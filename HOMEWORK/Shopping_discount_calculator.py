valid = False
while not valid:
    try:
        p = float(input("What is the price: "))
        d = float(input("What is the discount: "))
        n = int(input("How many people: "))
        d_p = p * d / 100
        d_p_f = p - d_p
        d_p_n = d_p_f / n
        valid = True
    except ZeroDivisionError:
        print("Choose a valid amount of people")
    except ValueError:
        print("Choose valid numbers")
    except:
        print("Wrong input")

a = "===================================="
print(a)
print("             TOTAL BILL             ")
print(f"Normal Price: {p}")
print(f"Discount Price: {d_p}")
print(f"Price Per Person: {d_p_n}")
print(a)