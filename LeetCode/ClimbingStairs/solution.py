class Solution:
    def climbStairs(self, n: int) -> int:
        """Using DP calculates the number of ways the
        staircase can be climbed

        Args:
            n (int): number of stairs

        Returns:
            int: maximum number of ways to climb the stairs
        """
        # initialise memo
        self.memo = {
            1: 1,
            2: 2
        }

        # call the recursive function
        return self.climb_recursive(n)
    

    def climb_recursive(self, num: int) -> int:
        """Recursively compute the maximum number of ways

        Args:
            num (int): number of stairs

        Returns:
            int: maximum ways for this subproblem
        """
        # check in memo
        max_ways = self.look_up_memo(num)
        if max_ways is not None:
            return max_ways
        
        # solve for num
        temp_max_ways = self.climb_recursive(num - 1) + self.climb_recursive(num - 2)
        self.add_to_memo(num, temp_max_ways)
        return temp_max_ways


    def look_up_memo(self, n: int) -> int:
        """Checks if this problem has been solved

        Args:
            n (int): number of stairs

        Returns:
            int: maximum number of ways (cached)
        """
        return self.memo.get(n)
    

    def add_to_memo(self, n: int, nfib: int) -> None:
        """Cache the solution for n stairs

        Args:
            n (int): number of stairs
            int: maximum number of ways (cached)
        """
        self.memo[n] = nfib
    
# for i in range(1, 6):
#     s = Solution()
#     print(s.climbStairs(i))