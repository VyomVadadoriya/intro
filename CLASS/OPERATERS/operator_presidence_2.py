number1 = int(input("Choose a number to check if it's divisible: "))

number2 = int(input("Choose a number to divide the first one by: "))

if number1 % number2 == 0:
    print("Your number is divisible by the second number")
else:
    print("Your number is not divisible by the second number")
