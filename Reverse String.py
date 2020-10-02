class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        count=0
        for chr in s:
            y= s.pop()
            s.insert(count,y)
            count+=1
        
