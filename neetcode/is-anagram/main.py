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

print("Neetcode Is Anagram")
sol = Solution()
s = "jam"
t = "jar"
res = sol.isAnagram(s,t)
print(res)