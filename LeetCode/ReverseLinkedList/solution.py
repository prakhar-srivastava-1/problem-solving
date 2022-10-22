# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head.next: return head

        # p, q, r
        # first element
        p = head
        # second element
        q = p.next

        while q:
            # third and temp element
            r = q.next

            q.next = p
            p = q
            q = r
        
        head = p
        return head


