class Solution:
    def findRelativeRanks(self, nums: List[int]) -> List[str]:
        
        s_nums= sorted(nums, reverse=True)
        
        output=[None]*len(nums)
        
        output[nums.index(s_nums[0])]="Gold Medal"
        if len(nums)>=2:
            output[nums.index(s_nums[1])]="Silver Medal"
        
        if len(nums)>=3:
            output[nums.index(s_nums[2])]="Bronze Medal"
        
        for i in range(3,len(nums)):
            output[nums.index(s_nums[i])]= str(i+1)
            
        return output
            
        
