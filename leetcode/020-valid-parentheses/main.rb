# @param {String} s
# @return {Boolean}
def is_valid(s)
  stack = []
  brackets_map = {
    ')' => '(',
    ']' => '[',
    '}' => '{'
  }

  s.each_char do |e|
    if brackets_map.values.include?(e)
      stack << e
    elsif brackets_map.keys.include?(e)
      return false if stack.empty? || stack.pop != brackets_map[e]
    end
  end
  
  return stack.empty?
end

s = "()"
puts is_valid(s)

s = "()[]{}"
puts is_valid(s)

s = "(]"
puts is_valid(s)