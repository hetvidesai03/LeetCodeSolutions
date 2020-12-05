class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        
        l=len(flowerbed)
        count=0
        
                    
        if(l==1):
            if(flowerbed[0]==1):
                count=0
            else:
                count=1
                
        if(l>1):
            if(flowerbed[0]==0 and flowerbed[1]==0):
                count+=1
                flowerbed[0]=1
                

            if(flowerbed[-1]==0 and flowerbed[-2]==0 ):
                count+=1
                flowerbed[-1]=1
                

            for i in range(1,l-1):

                if flowerbed[i-1]!=1 and flowerbed[i+1]!=1 and flowerbed[i]!=1:
                    count+=1
                    flowerbed[i]=1
       
        return count>=n
     
            
        
