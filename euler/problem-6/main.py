sqr_sum = 0
for i in range(1, 101):
    sqr_sum = sqr_sum + i
sqr_sum = pow(sqr_sum, 2)

sum_sqr = 0
for j in range(1, 101):
    sum_sqr = sum_sqr + pow(j, 2)

res = sqr_sum - sum_sqr
print(res)
