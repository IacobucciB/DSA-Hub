class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        srtd = sorted(nums)
        for i in range(len(nums) - 1):
            if srtd[i] == srtd[i+1]:
                res = srtd[i]
                return res
        return 0