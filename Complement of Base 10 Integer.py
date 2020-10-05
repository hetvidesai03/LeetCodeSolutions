class Solution:
    def bitwiseComplement(self, N: int) -> int:
        
        binary=bin(N).replace("0b", "") 
        x=""
        for i in range(len(binary)):
            
            if int(binary[i])==0:
                 x+="1"
            elif  int(binary[i])==1:
                 x+="0"
            

        return int(x,2)
        
