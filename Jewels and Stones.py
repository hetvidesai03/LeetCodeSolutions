class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        jewels= list(J)
        
        count=0;
        
        for i in S:
            if i in jewels:
                count+=1
                
        return count
