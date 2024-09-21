# @param {Integer[]} nums
# @param {Integer} target
# @return {Integer[]}
def two_sum(nums, target)
  seen = {}
  nums.each_with_index do |num, i|
    complement = target - num
    if seen.key?(complement)
      return [seen[complement], i]
    end
    seen[num] = i
  end
  return nil
end

puts "001-two-sum"
nums = [2,7,11,15]
target = 9
puts two_sum(nums,target)
