class Solution:
    def fib(self, n: int) -> int:
        """Computes the nth Fibonacci number

        Args:
            n (int): nth term of Fibonacci series

        Returns:
            int: Fibonacci Number
        """
        # if n = 0, 1 => 1   
        if n in (0, 1):
            return n
        
        # else F(n) = F(n-1) + F(n-2)     
        return self.fib(n-1) + self.fib(n-2)