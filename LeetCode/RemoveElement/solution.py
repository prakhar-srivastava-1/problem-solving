class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

        # corner case 
        # length = 1 and val = num[0] return 0
        # length = 1 and val != num[0] return 1
        if len(nums) == 1:
            if val == nums[0]: return 0
            if val != nums[0]: return 1

        # ptr to location where we will update the element
        ptr = 0

        for index, item in enumerate(nums):
            if item == val:
                continue
            # overwrite the element
            else:
                nums[ptr] = item
                ptr += 1

        return ptr