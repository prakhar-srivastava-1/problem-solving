class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        try:
            ans = 0
            if x > 0:
                ans = int(str(x)[::-1])
            elif x == 0:
                ans = 0
            elif x < 0:
                ans = -1 * int(str(x)[:0:-1])

            if ans >= -2147483648 and ans <= 2147483647:
                return ans
            else:
                return 0
        except:
            return 0