import math

def get_factors(number):
    factors = []
    for potential_factor in range(1, int(math.sqrt(number+1))):
        if number % potential_factor == 0:
            factors.append(potential_factor)
            factors.append(number // potential_factor)
    return factors

def is_prime(number):
    return len(get_factors(number)) == 2

number = 600851475143
all_factors = get_factors(number)
largest_prime_factor = 0
for factor in all_factors:
    if is_prime(factor) and factor > largest_prime_factor:
        largest_prime_factor = factor
print(largest_prime_factor)
