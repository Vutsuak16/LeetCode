# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head):
        
        if head==None:
            return None
        
        curr=head
        while curr != None:
            prev=curr
            while curr.next != None:
                if prev.val != curr.next.val:
                    break
                curr=curr.next
            prev.next=curr.next
            curr=curr.next
        return head