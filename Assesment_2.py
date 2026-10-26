try:
    num1 = float(input("What is the first number: "))
    num2 = float(input("What is the second number: "))
except ValueError:
    print("Enter valid numbers")
    exit()
except ZeroDivisionError:
    print("Can't enter zero")
    exit()
except:
    print("Not correct")
    exit()

def addition(num1 = 1, num2 = 1):
    return(num1 + num2)

def subtraction(num1 = 1, num2 = 1):
    return(num1 - num2)

def multiply(num1 = 1, num2 = 1):
    return(num1 * num2)

def divide(num1 = 1, num2 = 1):
    return(num1 / num2)
try:
    operation = input("What operation (addition, substraction, multiplication, division): ").lower()
except:
    print("Not correct")
    operation = "addition"

if operation == "addition":
    print(f"Your added result is {addition(num1, num2)}")
elif operation == "substraction":
    print(f"Your subtracted result is {subtraction(num1, num2)}")
elif operation == "multiplication":
    print(f"Your multiplied result is {multiply(num1, num2)}")
elif operation == "division":
    print(f"Your divided result is {divide(num1, num2)}")
else:
    print("Your operation was invalid")