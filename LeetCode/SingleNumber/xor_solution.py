class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]
        
        # using bitwise XOR => space complexity : O(1)
        result = 0
        
        for num in nums:
            result = result ^ num
        
        return result