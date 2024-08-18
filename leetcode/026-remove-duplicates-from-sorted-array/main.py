class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        if not nums:
            return 0
        k = 1
        for i in range(len(nums)-1,-1,-1):
            if nums[i] == nums[i-1]:
                k += 1
                nums[i] = "_"
                
        for _ in range(k):
            for i in range(len(nums)-1,0,-1):
                if nums[i-1] == "_":
                    nums[i-1] = nums[i]
                    nums[i] = "_"
        print(nums)
        return k


sol = Solution()
test = [1,1,2]
k = sol.removeDuplicates(test)
print(k)