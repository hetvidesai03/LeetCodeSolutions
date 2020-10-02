class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        dp= [[]for _ in range(target+1)]
        
        for c in candidates:
            for t in range(1,target+1):
                if c>t: continue
                if c==t: dp[t].append([c])
                for l in dp[t-c]:
                    dp[t].append(l+[c])
        return dp[-1]
