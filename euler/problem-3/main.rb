def trial_division(n)
  factors = []
  f = 2

  while f * f <= n
    if n % f == 0
      factors << f
      n /= f
    else
      f += 1
    end
  end
  factors << n if n != 1
  factors
end

number = 600851475143
res = trial_division(number)
puts res.inspect
