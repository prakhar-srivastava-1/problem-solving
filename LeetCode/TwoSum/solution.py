class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        complement = {}

        for index, item in enumerate(nums):
            if complement.get(item, (-1, False))[1]:
                return [complement.get(item)[0], index]
            complement[target - item] = (index, True)