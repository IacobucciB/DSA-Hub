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
        
        tags_count = len(strs)
        
        l = []
        
        l.append(strs[1])
        strs[1] = '#'
        tags_count--
        
        while tags_count > 0:
            for i in range(len(strs)):
                pass

        pass

strs = ["eat","tea","tan","ate","nat","bat"]