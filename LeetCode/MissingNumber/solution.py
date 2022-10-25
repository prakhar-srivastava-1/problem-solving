class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        len_nums = len(nums)

        # explicit check for 0
        if 0 not in nums: 
            return 0

        # calculate the sum
        sum_n = len_nums * (len_nums + 1) // 2

        # sum the list => O(n)
        sum_nums = sum(nums)

        # take difference = missing number
        return sum_n - sum_nums
        