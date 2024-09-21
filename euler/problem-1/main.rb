def sum_of_multiples(limit)
    total_sum = 0

    for x in 0..limit 
        if x % 3 == 0 or x % 5 == 0
            total_sum += x
        end
    end
    return  total_sum
end

result = sum_of_multiples(1000)
puts result
