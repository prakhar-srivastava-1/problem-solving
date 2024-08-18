class Solution:
    def rob(self, nums) -> int:
        """optimised solution using DP

        Args:
            nums (list[int]): amount of money of each house

        Returns:
            int: the maximum amount of money that can be robbed
        """
        # initialise memo
        self.memo = {}

        # call the recursive method
        return self.rob_houses(nums)


    def rob_houses(self, nums):
        """recursively find the max money by robbing
        non-adjacent houses 

        Args:
            nums (list[int]): amount of money of each house

        Returns:
            int: the maximum amount of money that can be robbed
        """
        # check the memo
        money = self.look_up_memo(nums)
        if money is not None:
            return money
        
        # if there is only one house
        if len(nums) == 1:
            return nums[0]

        # if length is 2 rob the bigger one
        if len(nums) == 2:
            return max(nums[0], nums[1])

        # either rob the current and leave the next
        # OR leave the current and start from next        
        temp_money = max(nums[0] + self.rob_houses(nums[2:]), self.rob_houses(nums[1:]))
        self.add_to_memo(nums, temp_money)
        # breakpoint()
        return temp_money


    def look_up_memo(self, nums) -> int:
        """checks if this subarray has already been solved (cached)

        Args:
            nums (list): list of houses

        Returns:
            int: maximum money that can be robbed from subarray (cached)
        """
        return self.memo.get(tuple(nums))

    def add_to_memo(self, nums, money) -> None:
        """add to cache (memoize) result of robbing a subarray of
        houses

        Args:
            nums (list): list of houses
            money (int): maximum money that can be robbed from subarray
        """
        self.memo[tuple(nums)] = money

# s = Solution()
# print(s.rob([1,2,3,1]))
# print(s.rob([2,7,9,3,1]))
# print(s.rob([104,209,137,52,158,67,213,86,141,110,151,127,238,147,169,138,240,185,246,225,147,203,83,83,131,227,54,78,165,180,214,151,111,161,233,147,124,143]))
# print(s.rob([2,1,1,2]))
# print(s.rob([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]))
