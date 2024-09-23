# @param {String[]} strs
# @return {String}
def longest_common_prefix(strs)
  return "" if strs.empty?
  
  min_len = strs.map { |str| str.length }.min
  result = ""
  
  for index in 0...min_len
    char = strs[0][index]
    all_match = strs.all? { |element| element[index] == char }
    
    if all_match
      result += char
    else
      break
    end
  end
  
  return result
end

strs = ["flower", "flow", "flight"]
puts longest_common_prefix(strs)

strs = ["dog", "racecar", "car"]
puts longest_common_prefix(strs)