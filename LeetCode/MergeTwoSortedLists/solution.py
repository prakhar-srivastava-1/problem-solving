# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        # if both are empty => return None
        if not (list1 or list2): return None

        # if list1 is empty => return list2
        if not list1: return list2

        # if list2 is empty => return list1
        if not list2: return list1
        
        # otherwise merge
        # intialise pointers
        ptr1, ptr2 = list1, list2
        # to save the sorted list
        ptr = head = None

        while ptr1 and ptr2:
            new_node = ListNode()
            if ptr1.val < ptr2.val:
                new_node.val = ptr1.val
                ptr1 = ptr1.next
            else:
                new_node.val = ptr2.val
                ptr2 = ptr2.next

            if not head:
                ptr = new_node 
                head = ptr
            else:
                ptr.next = new_node
                ptr = ptr.next
            
        while ptr2:
            # add ptr2 to the end
            ptr.next = ptr2
            ptr2 = ptr2.next
            ptr = ptr.next

        while ptr1:
            # add ptr1 to the end
            ptr.next = ptr1
            ptr1 = ptr1.next
            ptr = ptr.next

        return head