class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]
        
        # use a hashmap => space : O(n)
        num_count = {}

        for index, value in enumerate(nums):
            num_count[value] = num_count.get(value, 0) + 1
        
        for key, value in num_count.items():
            if value == 1:
                return key

        
