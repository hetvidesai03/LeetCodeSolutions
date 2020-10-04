class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        count=len(intervals)
        
        
        for xi, (xa,xb) in enumerate(intervals):
            for yi,(ya,yb) in enumerate(intervals):
        
                # decrease counter if interval can be covered
                if xi!=yi and ya<=xa<=xb<=yb:
                    count-=1
                    break
        return count
