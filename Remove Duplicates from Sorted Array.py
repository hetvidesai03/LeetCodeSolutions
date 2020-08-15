class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l=len(nums)
        s=0
        for i in range(l):
            if nums[i]!=nums[s]:
                s+=1
                nums[s]=nums[i]
        return s+1
