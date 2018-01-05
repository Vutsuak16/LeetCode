# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def oddEvenList(self, head):
        
        if head == None:
            return head
        odd=head
        even=head.next
        evenFirst=even
        while(1):
            if odd==None or even==None or even.next == None:
                odd.next=evenFirst
                break
            odd.next=even.next
            odd=even.next
            
            if odd.next == None:
                odd.next=evenFirst
                even.next=None
                break
            
            even.next=odd.next
            even=odd.next
        
        return head