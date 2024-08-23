class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        ctr = 0
        # repetitive division by 2
        while n != 0:
            d = n % 2
            if d == 1: ctr += 1 
            n = n // 2
        
        return ctr