class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        
        chr=""
        mx=0
        
        for i in range(len(releaseTimes)):
            diff= releaseTimes[i] - (i>0)*releaseTimes[i-1] 
            if diff>mx or diff==mx and keysPressed[i]>chr:
                chr=keysPressed[i]
                mx=diff
        return chr
        
        
        
