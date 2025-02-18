class Solution(object):

    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """

        if len(nums) == 0:
            return []

        hsh = {}
        res = []

        for n in nums:
            if n not in hsh:
                hsh[n] = 0
            hsh[n] += 1
        
        for i in range(0, k):
            m = 0
            c = 0
            for e in hsh.items():
                if e[1] > m:
                    m = e[1]
                    c = e[0]
            res.append(c)
            hsh[c] = -1

        return res

sol = Solution()
nums = [1,1,1,2,2,3]
k = 2
print(sol.topKFrequent(nums, k))

nums = [1]
k = 1
print(sol.topKFrequent(nums, k))

nums = [1,2]
k = 2
print(sol.topKFrequent(nums, k))
# [1,2]