class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        ans=[]
        max_candies=max(candies)
        for num in candies:
            if num+extraCandies>=max_candies:

                ans.append(True)
            else:

                ans.append(False)
        return ans
        
