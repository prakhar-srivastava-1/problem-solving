class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0: return False

        # else iterate over each power
        p = 0
        while True:
            num = 3 ** p

            if num == n:
                return True

            if num > n:
                return False
                
            p += 1