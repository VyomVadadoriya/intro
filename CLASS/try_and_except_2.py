try:
    num1 = int(input("FIRST NUMBER: "))
    num2 = int(input("SECOND NUMBER: "))
    result = num1/num2
except ZeroDivisionError:
    print("Division by zore is not allowed")
except ValueError:
    print("Enter valid numbers")
except:
    print("Wrong input")
else:
    print("No exceptions")
    print(result)
finally:
    print("\nRun no matter what")