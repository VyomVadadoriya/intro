import sys

sys.set_int_max_str_digits(0)  # Allow up to 100,000 digits

base = int(input("Enter the base: "))
exponent = int(input("Enter the exponent: "))

result = 1

for i in range(exponent):
    result *= base

print(f"{base} to the power of {exponent} = {result}")
