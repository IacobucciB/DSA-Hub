def sum_of_multiples(limit):
    total_sum = 0
    
    for x in range(limit):
        if x % 3 == 0 or x % 5 == 0:
            total_sum += x
            
    return total_sum

result = sum_of_multiples(1000)
print(result)
