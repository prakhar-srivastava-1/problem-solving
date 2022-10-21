class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # count 0's
        ctr = nums.count(0)
        n = ctr

        # remove each 0
        while n != 0:
            n -= 1 
            nums.remove(0)

        # append 0's to the end of list
        nums[:] = nums + [0] * ctr
