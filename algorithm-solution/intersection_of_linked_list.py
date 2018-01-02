# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        
        if headA==None or headB==None:
            return None
        
        ct1=0
        l=headA
        while l!=None:
            l=l.next
            ct1+=1
        ct2=0
        l=headB
        while l!=None:
            l=l.next
            ct2+=1
        if ct1-ct2<0:
            ct=ct2-ct1
            l=headB
            while ct!=0:
                l=l.next
                ct-=1
            head1=headA
            head2=l
            while head1!=None and head2!=None:
                if head1==head2:
                    return head1
                head1=head1.next
                head2=head2.next
            
        elif ct1-ct2>0:
            ct=ct1-ct2
            l=headA
            while ct!=0:
                l=l.next
                ct-=1
            head1=headB
            head2=l
            while head1!=None and head2!=None:
                if head1==head2:
                    return head1
                head1=head1.next
                head2=head2.next
        else:
            head1=headB
            head2=headA
            while head1!=None and head2!=None:
                if head1==head2:
                    return head1
                head1=head1.next
                head2=head2.next
        return None