'''
Given a linked list, swap every two adjacent nodes and return its head.

For example,
Given 1->2->3->4, you should return the list as 2->1->4->3.

Your algorithm should use only constant space. 

You may not modify the values in the list, only nodes itself can be changed.

'''


class Solution(object):
    def swapPairs(self, head):
        
        if head == None:
            return head
        
        if head.next == None:
            return head
        
        curr=head
        ct=1
        while curr.next != None:
            if ct%2 != 0:
                curr.val,curr.next.val=curr.next.val,curr.val
                if ct==1:
                    head=curr
            ct+=1
            curr=curr.next
        
        return head
                
            