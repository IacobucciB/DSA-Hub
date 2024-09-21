# @param {Integer[]} nums
# @param {Integer} target
# @return {Integer[]}
def two_sum(nums, target)
  for i in 0..nums.length
    for j in i+1..(nums.length-1)
      if (nums[i] + nums[j]) == target
        return [i, j]
      end
    end
  end
  return []
end

puts "001-two-sum"
nums = [2,7,11,15]
target = 9
puts two_sum(nums,target)
