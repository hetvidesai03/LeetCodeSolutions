class Solution:
    def bagOfTokensScore(self, tokens: List[int], P: int) -> int:
        
        ans=0
        
        while ans>0 or tokens and P>=min(tokens):
            
            if tokens and P >= min(tokens):
                P -= min(tokens)
                tokens.remove(min(tokens))
                ans += 1
            
            elif ans>0 and len(tokens)>1:
                ans -=1
                P +=max(tokens)
                tokens.remove(max(tokens))
            else:
                break
        
        return ans
               
