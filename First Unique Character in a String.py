class Solution:
    def firstUniqChar(self, s: str) -> int:
        
        for index in range(len(s)):
            if s.count(s[index])==1:
                return index
        return -1        
