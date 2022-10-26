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
        ptrA, ptrB = headA, headB
        
        # hash table
        # ListNode : visited
        common = {}
        
        # fill the table
        while ptrA:
            common[ptrA] = 1
            ptrA = ptrA.next

        # if value is mapped in common and the pointers match => return node
        while ptrB:
            if common.get(ptrB, 0) == 1:
                return ptrB
            ptrB = ptrB.next
        
        # if no intersection 
        return None