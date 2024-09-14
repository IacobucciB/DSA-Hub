class Solution:
    def hasDuplicate(self, nums: list[int]) -> bool:
        srtd = sorted(nums)
        for i in range(len(nums) - 1):
            if srtd[i] == srtd[i+1]:
                return True
        return False

sol = Solution()
nums = [1, 2, 3, 3]
res = sol.hasDuplicate(nums)
print(res)