class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # memo to save the seen numbers
        complement = {}

        for index, item in enumerate(nums):
            # if number is found
            if complement.get(item, (-1, False))[1]:
                return [complement.get(item)[0], index]
            # otherwise add to the memo
            complement[target - item] = (index, True)