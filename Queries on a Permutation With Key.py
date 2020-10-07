class Solution:
    def processQueries(self, queries: List[int], m: int) -> List[int]:
        
        arr= list(range(1,m+1))
        ans=[]
        for i in queries:
            
            ans.append(arr.index(i))
            arr.insert(0,arr.pop(arr.index(i)))
        
        return ans
