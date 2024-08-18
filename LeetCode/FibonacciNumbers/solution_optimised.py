class Solution:
    def fib(self, n: int) -> int:
        """Computes the nth Fibonacci number using
        Dynamic Programming

        Args:
            n (int): nth term of Fibonacci series

        Returns:
            int: Fibonacci Number
        """
        # initialise memo
        self.memo = {
            0: 0,
            1: 1,
        }

        # call the recursive function
        return self.fib_recursive(n)
    

    def fib_recursive(self, nfib:int) -> int:
        """Computes the nth Fibonacci number using
        recursion

        Args:
            n (int): nth term of Fibonacci series

        Returns:
            int: Fibonacci Number
        """
        # check the memo
        num = self.look_up_memo(nfib)
        if num is not None:
            return num
        
        # else F(n) = F(n-1) + F(n-2)     
        temp_fib = self.fib_recursive(nfib-1) + self.fib_recursive(nfib-2)
        self.add_to_memo(nfib, temp_fib)
        return temp_fib


    def look_up_memo(self, n: int) -> int:
        """Checks if fibonacci number has been cached

        Args:
            n (int): nth term of Fibonacci series

        Returns:
            int: Fibonacci Number (from cache)
        """
        return self.memo.get(n)
    

    def add_to_memo(self, n: int, nfib: int) -> None:
        """Cache the nth term if not already in memo

        Args:
            n (int): nth term of Fibonacci series
            nfib (int): Fibonacci Number
        """
        self.memo[n] = nfib


# for i in range(6):
#     s = Solution()
#     print(i, s.fib(i))