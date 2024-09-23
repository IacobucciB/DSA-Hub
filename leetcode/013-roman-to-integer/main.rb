# @param {String} s
# @return {Integer}
def roman_to_int(s)
  roman_values = {
    'I' => 1,
    'V' => 5,
    'X' => 10,
    'L' => 50,
    'C' => 100,
    'D' => 500,
    'M' => 1000
  }
  total = 0
  pre_value = 0
  s.reverse.each_char do |numeral|
    value = roman_values[numeral]
    if value < pre_value
      total = total - value
    else
      total = total + value
      pre_value = value
    end
  end
  return total
end

s = "III"
puts roman_to_int(s)

s = "LVIII"
puts roman_to_int(s)

s = "MCMXCIV"
puts roman_to_int(s)
