# @param {Integer} x
# @return {Boolean}
def is_palindrome(x)
  if (x.to_s == x.to_s.reverse)
    return true
  end
  return false
end

x = 121
res = is_palindrome(x) 
puts res.inspect

x = -121
res = is_palindrome(x) 
puts res.inspect

x = 10
res = is_palindrome(x) 
puts res.inspect
