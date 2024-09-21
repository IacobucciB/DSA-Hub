def sum_of_even_fibo(limit)
  a, b = 1, 2
  total = 0
  while a <= limit
    total += a if a.even?
    a, b = b, a + b
  end
  return total
end

limit = 4000000
res = sum_of_even_fibo(limit)
puts res