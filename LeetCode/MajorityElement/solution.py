class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        set_nums = set(nums)

        # O(n) time; O(n) space
        count_dict = {digit: nums.count(digit) for digit in set_nums}
        print(count_dict)

        # sentinel
        max_value = count_dict[nums[0]]
        max_key = nums[0]

        # O(n)
        for key, value in count_dict.items():
            if value > max_value:
                max_key = key
                max_value = value
            
        return max_key