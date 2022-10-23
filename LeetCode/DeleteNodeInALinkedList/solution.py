# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        # no need to check empty or single node list 
        # as there will always be 2 nodes atleast
        node.val = node.next.val
        node.next = node.next.next
        
