import math

# Helper function to generate a list of primes up to a limit using Sieve of Eratosthenes
def sieve_of_eratosthenes(limit):
    sieve = [True] * (limit + 1)
    sieve[0] = sieve[1] = False
    for start in range(2, int(math.sqrt(limit)) + 1):
        if sieve[start]:
            for i in range(start * start, limit + 1, start):
                sieve[i] = False
    primes = [num for num, is_prime in enumerate(sieve) if is_prime]
    return primes

# Function to check if a number is prime and return the first prime factor found
def first_prime_factor(p):
    # Step 1: Handle small primes up to 100
    small_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 
                   53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    
    # If p is divisible by any small prime, return that prime factor
    for prime in small_primes:
        if p % prime == 0:
            return prime  # Return the first prime factor found
    
    # Step 2: Calculate sqrt(p) and sqrt(sqrt(p))
    sqrt_p = math.sqrt(p)
    sqrt_sqrt_p = math.sqrt(sqrt_p)

    digits = 0
    digitCounter = p
    if(digitCounter == 0):
        return -1

    while(digitCounter != 0):
        digitCounter = digitCounter // 10
        digits += 1
    
    # Step 3: Define the range dynamically based on the size of p
    # The scaling factor is proportional to the size of p
    if p < 10**6:
        start = int(sqrt_sqrt_p)
        end = int(sqrt_p)
    else:
        # For large numbers, scale the range dynamically
        scaling_factor = math.pow(10, (digits / 5))
        start = int(sqrt_sqrt_p)
        end = int(scaling_factor * sqrt_sqrt_p)

    # Step 4: Generate primes in the range from sqrt(sqrt(p)) to sqrt(p)
    primes_in_range = sieve_of_eratosthenes(end)
    primes_in_range = [prime for prime in primes_in_range if prime >= start]
    
    # Step 5: Test divisibility by these primes and return the first prime factor
    for prime in primes_in_range:
        if p % prime == 0:
            return prime  # Return the first prime factor found

    print(f"{end}")
    return None  # p is prime, no factors found

# Test the function
# ((2^49) - 1) is prime?
# ((2^53) - 1) seems to be max power of 2 testable.
# test_numbers = [29, 1009, 10007, 987654321, (2**400) - 1)]
test_numbers = [(2**100) - 1]
for number in test_numbers:
    result = first_prime_factor(number)
    sq_sq_p = math.sqrt(math.sqrt(number))
    print(f"{sq_sq_p} is the square square root\n")
    if result is None:
        print(f"{number} is prime.")
    else:
        print(f"First prime factor of {number} is {result}.")
