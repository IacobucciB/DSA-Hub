def trial_division(n: int) -> list[int]:
    a = []
    f = 2

    while f*f <= n:
        if n % f == 0:
            a.append(f)
            n //= f
        else:
            f += 1
    if n != 1:
        a.append(n)
    return a

number: int = 600851475143
res = trial_division(number)
print(res)
