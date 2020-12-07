class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        
        sPoints = sorted(x for x,y in points)
        
        diff=0
        print(sPoints)
        for index in range(0,len(sPoints)-1):
            
            if sPoints[index+1]-sPoints[index]>diff:
                diff=sPoints[index+1]-sPoints[index]
        return diff
