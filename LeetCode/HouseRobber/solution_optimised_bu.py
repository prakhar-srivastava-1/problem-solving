class Solution:
    def rob(self, nums) -> int:
        """optimised solution using DP (bottom-up)

        Args:
            nums (list[int]): amount of money of each house

        Returns:
            int: the maximum amount of money that can be robbed
        """
        # capture in a variable to avoid multiple function calls
        len_nums = len(nums)

        # if there is only one house
        if len_nums == 1:
            return nums[0]
        
        # if there are only 2 houses
        if len_nums == 2:
            return max(nums)
        
        # initialise memo
        # memo tracks the max money we can accumulate until that index
        # add 0th and 1st element to memo as starting points
        self.memo = [0] * len_nums
        self.memo[0] = nums[0]
        self.memo[1] = max(self.memo[0], nums[1])

        # build the solution
        for i in range(2, len_nums):
            # breakpoint()
            self.memo[i] = max(
                # take the current element and
                # add with max until last to previous house
                self.memo[i-2] + nums[i],
                # ignore the current element
                # and keep the max until previous house
                self.memo[i-1]
            )

        # return the last entry of memo
        return self.memo[-1]

# s = Solution()
# print(s.rob([1,2,3,1]))
# print(s.rob([2,7,9,3,1]))
# print(s.rob([104,209,137,52,158,67,213,86,141,110,151,127,238,147,169,138,240,185,246,225,147,203,83,83,131,227,54,78,165,180,214,151,111,161,233,147,124,143]))
# print(s.rob([2,1,1,2]))
# print(s.rob([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]))
