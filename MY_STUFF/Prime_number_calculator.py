def find_primes(start, end):
    primes = []
    
    for num in range(start, end + 1):
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                primes.append(num)
                
    return primes

# Example: Find primes between 10 and 30
print(find_primes(100, 150))
# Output: [11, 13, 17, 19, 23, 29]
