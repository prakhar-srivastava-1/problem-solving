# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # c => carry
        c = 0
        
        # ans variable to store the final answer
        # keep concatenating the digits and reverse
        # in the end
        head = ans = ListNode()

        # construct numbers
        head_l1 = l1
        num1 = ""
        while l1:
            num1 = num1 + str(l1.val)
            l1 = l1.next
        num1 = num1[::-1]
        
        head_l2 = l2
        num2 = ""
        while l2:
            num2 = num2 + str(l2.val)
            l2 = l2.next
        num2 = num2[::-1]

        head = ans = ListNode()
        num = str(int(num1) + int(num2))
        
        for index, each in enumerate(num[::-1]): 
            ans.val = int(each)
            if len(num) - 1 == index:
                break
            ans.next = ListNode()
            ans = ans.next
        
        return head
            