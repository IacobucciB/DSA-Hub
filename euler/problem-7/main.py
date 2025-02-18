import math

def get_factors(number):
    factors = []
    for potential_factor in range(1, int(math.sqrt(number)) + 1):
        if number % potential_factor == 0:
            factors.append(potential_factor)
            if potential_factor != number // potential_factor:
                factors.append(number // potential_factor)
    return factors

def is_prime(number):
    return len(get_factors(number)) == 2

counter = 1
n = 1
while counter <= 10_001:
    n = n + 1
    if is_prime(n):
        counter = counter + 1

print(n)  
