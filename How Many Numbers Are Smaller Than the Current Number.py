class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        
        s_nums=sorted(nums)
        
        return list(map(lambda x: s_nums.index(x),nums))
