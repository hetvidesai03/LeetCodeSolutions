class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        
        matrix=[[0] * n for x in range(n)]
        
        top=0
        right=n-1
        left=0
        bottom=n-1
        num=1
        
        while top<=bottom and left<=right:
            
            for i in range(left,right+1):
                matrix[top][i]=num
                num+=1
            top+=1
            
            for j in range(top,bottom+1):
                matrix[j][right]=num
                num+=1
                
            right-=1
            
            for k in range(right,left-1,-1):
                matrix[bottom][k]=num
                num+=1
            
            bottom-=1
            
            for l in range(bottom,top-1,-1):
                matrix[l][left]=num
                num+=1
            
            left+=1
        
        return matrix
                
        
