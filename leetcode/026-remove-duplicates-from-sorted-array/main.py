class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        if not nums:
            return 0
        k = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[k] = nums[i]
                k += 1
        return k

sol = Solution()
test = [0,0,1,1,1,2,2,3,3,4]
k = sol.removeDuplicates(test)
print(k)