class Solution:
    def fib(self, n: int) -> int:
        """Computes the nth Fibonacci number using
        Dynamic Programming

        Args:
            n (int): nth term of Fibonacci series

        Returns:
            int: Fibonacci Number
        """
        self.memo = {
            0: 0,
            1: 1,
            2: 1,
        }

        num = self.look_up_memo(n)
        if num is not None:
            return num
        
        else:
            # else F(n) = F(n-1) + F(n-2)     
            temp_fib = self.fib(n-1) + self.fib(n-2)
            return self.add_to_memo(n, temp_fib)
    

    def look_up_memo(self, n: int) -> int:
        """Checks if fibonacci number has been cached

        Args:
            n (int): nth term of Fibonacci series

        Returns:
            int: Fibonacci Number (from cache)
        """
        return self.memo.get(n)
    

    def add_to_memo(self, n: int, nfib: int) -> int:
        """Cache the nth term if not already in memo

        Args:
            n (int): nth term of Fibonacci series
            nfib (int): Fibonacci Number

        Returns:
            int: Fibonacci Number (after caching)
        """
        self.memo[n] = nfib
        return nfib