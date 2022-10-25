class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        # a dict to store data in following format
        # target - item: (index, True/False)
        complement = {}

        for index, item in enumerate(numbers):
            # if item in complement - check 1st index of tuple
            if complement.get(item, (-1, False))[1]:
                return [complement.get(item)[0] + 1, index + 1]
            # else - add the complement of item into the dict
            complement[target - item] = (index, True)