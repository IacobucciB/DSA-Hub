class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_sortd = sorted(s)
        t_sortd = sorted(t)
        for i in range(len(s)):
            if s_sortd[i] != t_sortd[i]:
                return False
        return True

    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:

        res = {}

        for word in strs:
            aux = ''.join(sorted(word))

            if aux not in res:
                res[aux] = []

            res[aux].append(word) 
        
        return list(res.values())

sol = Solution()

strs = ["eat","tea","tan","ate","nat","bat"]

r = sol.groupAnagrams(strs)

print(r)