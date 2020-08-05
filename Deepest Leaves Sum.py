# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        
        previous_level=[]
        current_traversal=[root]
        
        while current_traversal:
            
            next_level=[]
            
            for node in current_traversal:
                
                if node.left:
                    next_level.append(node.left)
                
                if node.right:
                    next_level.append(node.right)
                    
            previous_level=current_traversal
            current_traversal= next_level
            
        return sum( node.val for node in previous_level if node )