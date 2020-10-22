class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        
        seq= set()
        rep_seq= set()
        
        for index in range(len(s)-9):
            
            check_seq= s[index:index+10]
            
            if check_seq in seq:
                rep_seq.add(check_seq)
            
            seq.add(check_seq)
        
        return list(rep_seq)
