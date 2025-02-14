def sum_of_even_fibo(limit):
    a, b = 1, 2
    total = 0
    while a <= limit:
        if a % 2 == 0:
            total += a
        a, b = b, a + b
    return total
        

limit = 4000000
res = sum_of_even_fibo(limit)
print(res)