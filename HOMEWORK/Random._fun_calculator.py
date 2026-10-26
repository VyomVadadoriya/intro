import random
import math

number = random.randint(1, 10)
print("Your lucky number is:", number)

fun_choices = ["Play a game", "Solve a puzzle", "Read a story", "Draw something"]
activity = random.choice(fun_choices)
print("Random activity for today:", activity)

print("\nGuess the secret number from 1 to 5")
secret_number = random.randint(1, 5)

while True:
    guess = int(input("Enter your guess: "))

    if guess == secret_number:
        print("Correct you guessed the number.")
        break
    else:
        print("Wrong guess. Try again!")

decimal_number = float(input("\nEnter a decimal number: "))

print("Ceiling value:", math.ceil(decimal_number))
print("Floor value:", math.floor(decimal_number))
x = 10
y = -5
print("Copy sign result:", math.copysign(x, y))
negative_number = int(input("Enter a negative number: "))
print("Absolute value:", math.fabs(negative_number))

num1 = int(input("Enter first number for GCD: "))
num2 = int(input("Enter second number for GCD: "))

print("GCD is:", math.gcd(num1, num2))

print("\n===== FUN CALCULATOR SUMMARY =====")
print("Lucky Number:", number)
print("Random Activity:", activity)
print("Secret Number:", secret_number)
print("==================================")