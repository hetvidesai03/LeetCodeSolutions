# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        
    
        node=head
        list_len=1
        
        if not head or not head.next:
            return head
        
        while(node.next is not None):
            node=node.next
            list_len+=1
          
        
        node=head
        xnode=None
        for i in range(k%list_len):
            while node.next:
                xnode=node
                node=node.next
            node.next=head
            head=node
            xnode.next=None
        return head 
