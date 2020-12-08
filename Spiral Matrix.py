class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        element=[]
        if not matrix:
            return element
            
        top,right,bottom,left=0,len(matrix[0])-1,len(matrix)-1,0
        
        while top<=bottom or left<=right:
            
            if top<=bottom:
                for i in range(left,right+1):
                    element.append(matrix[top][i])
            top+=1
            
            if left<=right:
                for j in range(top,bottom+1):
                    element.append(matrix[j][right])


            right-=1

            if top<=bottom:
                for k in range(right,left-1,-1):
                    element.append(matrix[bottom][k])


            bottom-=1
            
            if left<=right:
                for l in range(bottom,top-1,-1):
                    element.append(matrix[l][left])


            left+=1
        return element
        
