class Solution(object):
    def reverseList(self, head):
        
        if head ==None:
            return None
        else:
            curr=head
            prev=None
            while curr != None:
                next_=curr.next
                curr.next=prev
                prev=curr
                curr=next_
            head=prev
            return head
        