class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        
        counter = collections.Counter(nums)
        c=0
        
        for count in counter.values():
            if count > 1:
                c+=math.comb(count, 2)
        return c
