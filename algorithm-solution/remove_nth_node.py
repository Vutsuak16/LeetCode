# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        l=head
        while l != None:
            l=l.next
        l=head
        if head == None:
            return None
        ct=0
        while l != None:
            l=l.next
            ct+=1
        l=head
        ct2=0
        prev=None
        while ct2 != (ct-n):
            prev=l
            l=l.next
            ct2+=1
        
        if prev==None:
            head=head.next
            return  head    
        
        ct3=ct2+2
        print ct,ct2,ct3
        print prev.val
        if ct3>ct:
            prev.next=None
            return head
        
        
        l=head
        ct4=1
        while  ct4 != ct3:
            ct4+=1
            if l.next == None:
                break
            l=l.next
            
        last=l
        prev.next=last
        return head
        
        
        
        
            