# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        
        if head == None:
            return True
        
        curr=head
        ct=0
        while curr != None:
            curr=curr.next
            ct+=1
            
        if ct%2==0:
            ct_even=ct/2
            l=head
            prev=None
            curr=head
            while ct_even != 0:
                next_= curr.next
                curr.next=prev
                prev=curr
                curr=next_
                ct_even-=1
            while prev != None:
                if prev.val != curr.val:
                    return False
                prev=prev.next
                curr=curr.next
        else:
            ct_odd=ct//2
            l=head
            prev=None
            curr=head
            while ct_odd != 0:
                next_= curr.next
                curr.next=prev
                prev=curr
                curr=next_
                ct_odd-=1
            curr=curr.next
            while prev != None:
                if prev.val != curr.val:
                    return False
                prev=prev.next
                curr=curr.next
        return True
            
        
        
        