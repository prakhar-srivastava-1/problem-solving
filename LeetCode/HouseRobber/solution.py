class Solution:
    def rob(self, nums) -> int:
        """recursively find the max money by robbing
        non-adjacent houses

        Args:
            nums (list[int]): amount of money of each house

        Returns:
            int: the maximum amount of money that can be robbed
        """
        # if there is only one house
        if len(nums) == 1:
            return nums[0]

        # if length is 2 rob the bigger one
        if len(nums) == 2:
            return max(nums[0], nums[1])

        # either rob the current and leave the next
        # OR leave the current and start from next        
        return max(nums[0] + self.rob(nums[2:]), self.rob(nums[1:]))

# s = Solution()
# print(s.rob([1,2,3,1]))
# print(s.rob([2,7,9,3,1]))
# print(s.rob([104,209,137,52,158,67,213,86,141,110,151,127,238,147,169,138,240,185,246,225,147,203,83,83,131,227,54,78,165,180,214,151,111,161,233,147,124,143]))
