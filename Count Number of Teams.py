class Solution:
    def numTeams(self, rating: List[int]) -> int:
        
        from itertools import combinations
        count=0
        
        comb = list(combinations(rating,3))
        
        for pair in comb:
            if pair[0]<pair[1]<pair[2] or pair[0]>pair[1]>pair[2]:
                count+=1
        return count
