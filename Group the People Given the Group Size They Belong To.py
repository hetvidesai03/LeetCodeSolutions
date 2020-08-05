class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        
        temp = {}
        groups = []
        
        for i, size in enumerate(groupSizes):
            temp[size] = temp.get(size, []) + [i]
            if len(temp[size]) == size:
                groups += [temp.pop(size)]
        return groups