class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # if set and list lengths are unequal => False
        # otherwise True
        return len(set(nums)) < len(nums)