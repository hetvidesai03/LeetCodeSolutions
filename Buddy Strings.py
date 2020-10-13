class Solution:
    def buddyStrings(self, A: str, B: str) -> bool:
        
        if A==B:
            return len(A)-len(set(A))>=1
        
        elif set(A)==set(B) and len(A)==len(B):
            count=0
            x=[]
            for i in range(len(A)):
               
                if A[i]!=B[i]:
                    count+=1
                    x.append(i)
                if count >=3:
                    return False
            
            if count==1:
                return False
            elif A[x[0]]==B[x[1]] and A[x[1]]==B[x[0]]:
                return True
