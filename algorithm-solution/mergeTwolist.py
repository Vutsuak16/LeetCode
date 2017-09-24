# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        
        l=[]
        if l1==None:
            return l2
        elif l2==None:
            return l1
        else:
            while True:
                
                if l1.val<l2.val:
                    l.append(l1.val)
                    l1=l1.next
                else:
                    l.append(l2.val)
                    l2=l2.next
                if l1 is None or l2 is None:
                    break
            
            if l1 != None:
                while l1 !=None:
                    l.append(l1.val)
                    l1=l1.next
            else:
                while l2 !=None:
                    l.append(l2.val)
                    l2=l2.next
            return l